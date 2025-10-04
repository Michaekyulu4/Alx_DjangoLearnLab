from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Auth: login & logout using built-in views
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logged_out.html"), name="logout"),

    # Register and profile
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    # Blog post CRUD
    path("", views.PostListView.as_view(), name="post-list"),
    path("post/new/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),

    # Comments
      path("post/<int:post_pk>/comments/new/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comments/<int:pk>/edit/", views.CommentUpdateView.as_view(), name="comment-update"),
    path("comments/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
]
