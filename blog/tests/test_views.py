# mypy: disable-error-code="attr-defined"

import json

from django.contrib.auth import get_user_model
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from blog.models import Post

fake = Faker()
User = get_user_model()


class TestPostListAPIView(APITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.password = fake.password()
        cls.user = User.objects.create_user(
            email=fake.email(), password=cls.password
        )
        cls.post = Post.objects.create(
            author=cls.user,
            content=fake.text(),
        )

    def test_get_posts(self) -> None:
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        count = Post.objects.count()
        self.assertEqual(len(response.data), count)
        json_response = response.json()[0].get("content")
        self.assertEqual(self.post.content, json_response)


class TestPostDetailAPIView(APITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.password = fake.password()
        cls.user = User.objects.create_user(
            email=fake.email(), password=cls.password
        )
        cls.post = Post.objects.create(
            author=cls.user,
            content=fake.text(),
        )

    def test_get_post(self) -> None:
        response = self.client.get(
            reverse(
                "episode",
                kwargs={"episode_number": self.post.episode_number},
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            self.post.content, json.loads(response.content).get("content")
        )
