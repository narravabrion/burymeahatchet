from rest_framework import serializers

from blog.models import Post


class BlogSerializer(serializers.ModelSerializer[Post]):
    class Meta:
        model = Post
        fields = [
            "id",
            "episode_number",
            "content",
            "created_at",
            "updated_at",
        ]
