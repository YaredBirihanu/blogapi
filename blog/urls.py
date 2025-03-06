from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from .views import NotificationListView,notification_test


from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikeViewSet,ProfilViewset

router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('likes', LikeViewSet)
router.register('profils',ProfilViewset)

urlpatterns = [
    path('',include(router.urls)),

    path('notifications/', NotificationListView.as_view(), name='notification-list'),
     path('notification-test/', notification_test, name='notification-test'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
]
