from django.urls import path

from blog.views import BlogDetailView, BlogListView

urlpatterns = [
    path("posts/", BlogListView.as_view(), name="posts"),
    path(
        "posts/<int:episode_number>/episodes/",
        BlogDetailView.as_view(),
        name="episode",
    ),
]
