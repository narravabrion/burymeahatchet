from rest_framework import generics

from blog.models import Post
from blog.serializers import BlogSerializer


# view that only allows to get blogs
class BlogListView(generics.ListAPIView[Post]):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer


# get a specific blog
class BlogDetailView(generics.RetrieveAPIView[Post]):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "episode_number"
    lookup_url_kwarg = "episode_number"
