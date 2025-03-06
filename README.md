# Blog API with Django Rest Framework (DRF)

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django%20Rest%20Framework-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)

A production-ready **Blog API** built with Django Rest Framework (DRF). This project demonstrates my expertise in building RESTful APIs, implementing authentication, handling file uploads, and integrating advanced features like real-time notifications.

---

## Features

- **User Authentication**: JWT-based authentication for secure user login and registration.
- **Blog Posts**: CRUD operations for blog posts with image uploads.
- **Comments**: Add, update, and delete comments on blog posts.
- **Likes**: Like/unlike blog posts.
- **Real-Time Notifications**: Notify users in real-time using WebSockets.
- **Pagination**: Paginate blog posts and comments for better performance.
- **Rate Limiting**: Prevent API abuse with rate limiting.
- **Testing**: Comprehensive unit and integration tests.
- **Deployment**: Ready for deployment with production-ready settings.

---

## Technologies Used

- **Backend**: Django, Django Rest Framework (DRF)
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Real-Time Communication**: Django Channels, WebSockets
- **File Storage**: Local storage (for development), AWS S3 (for production)
- **Testing**: Django Test Framework, pytest
- **Deployment**: Docker, Heroku/AWS

---

## API Endpoints

| **Endpoint**               | **Method** | **Description**                          |
|----------------------------|------------|------------------------------------------|
| `/api/register/`           | POST       | Register a new user.                     |
| `/api/token/`              | POST       | Obtain JWT token for authentication.     |
| `/api/token/refresh/`      | POST       | Refresh JWT token.                       |
| `/api/posts/`              | GET, POST  | List all posts or create a new post.     |
| `/api/posts/{id}/`         | GET, PUT, DELETE | Retrieve, update, or delete a post. |
| `/api/posts/{id}/comments/`| GET, POST  | List all comments or add a new comment.  |
| `/api/posts/{id}/like/`    | POST       | Like or unlike a post.                   |
| `/api/notifications/`      | GET        | List all notifications for the user.     |
| `/ws/notifications/`       | WebSocket  | Real-time notifications.                 |

---

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL
- Redis (for real-time notifications)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name


