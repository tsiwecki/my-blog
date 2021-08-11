from django.urls import path
from .views import (
    BlogListView, 
    BlogDetailView, 
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)


urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("posts/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name='post_delete'),
]