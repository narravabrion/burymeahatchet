from django.test import TestCase
from faker import Faker

from blog.models import Post

fake = Faker()


class PostModelTest(TestCase):
    post: Post

    def setUp(self) -> None:
        self.data = {
            "content": fake.text(),
        }

    # @classmethod
    # def setUpTestData(cls) -> None:
    #     super().setUpClass()
    #     data = {
    #         "content": fake.text(),
    #     }
    #     cls.post = Post.objects.create(**data)

    def test_create_post(self) -> None:
        post = Post.objects.create(**self.data)
        self.assertEqual(post.content, self.data["content"])
        self.assertEqual(post.episode_number, 1)
        self.assertEqual(post.author, None)
