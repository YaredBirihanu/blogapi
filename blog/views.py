from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment, Like,Profile,Notification
from .serializers import PostSerializer, CommentSerializer, LikeSerializer,ProfileSerializer,UserSerializer,NotificationSerializer


def notification_test(request):
    return render(request, 'notifications.html')


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    '''the perform_create method is used to set the author 
    field of the new Post instance to the currently authenticated 
    user making the request. This ensures that each post is associated
    with the user who created it.
    -associating a post with the user who created it.
    '''
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post__title', 'post__author']

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def perform_create(self, serializer):
        post = serializer.validated_data['post']
        user = self.request.user
        serializer.save(user=user)

        # Send notification to the post author
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'notifications_{post.author.id}',
            {
                'type': 'send_notification',
                'message': f'{user.username} liked your post: {post.title}',
            }
        )


class ProfilViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        Profile.objects.create(user=user)


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)