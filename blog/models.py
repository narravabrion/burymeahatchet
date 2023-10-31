import uuid
from typing import Any

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    episode_number = models.PositiveIntegerField(unique=True, editable=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args: Any, **kwargs: Any) -> None:
        if not self.episode_number:
            last_episode = Post.objects.all().order_by("episode_number").last()
            if last_episode:
                self.episode_number = last_episode.episode_number + 1
            else:
                self.episode_number = 1
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering: list[str] = ["episode_number"]

    def __str__(self) -> str:
        return self.content[:10]
