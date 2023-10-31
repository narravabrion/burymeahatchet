from typing import Any

from django.contrib.auth import get_user_model
from django.test import TestCase
from faker import Faker

fake = Faker()

User = get_user_model()


class UsersManagerTests(TestCase):
    def test_create_user(self) -> None:
        email = fake.email()
        password = fake.password()
        user = User.objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertFalse(user.is_admin)

        with self.assertRaises(TypeError):
            User.objects.create_user()  # type: ignore[call-arg]
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")  # type: ignore[call-arg]
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password=fake.password())

    def test_create_superuser(self) -> None:
        data = {
            "email": fake.email(),
            "password": fake.password(),
        }
        admin_user = User.objects.create_superuser(
            **data,
        )
        self.assertEqual(admin_user.email, data["email"])
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_admin)


class UserModelTest(TestCase):
    user: Any

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        data = {
            "email": fake.email(),
            "password": fake.password(),
        }

        cls.user = User.objects.create_user(**data)

    def test_create_user(self) -> None:
        data = {
            "email": fake.email(),
            "password": fake.password(),
        }
        user = User.objects.create_user(**data)
        self.assertEqual(user.email, data["email"])

    def test_password_exception_raised(self) -> None:
        with self.assertRaises(ValueError):
            User.objects.create_user(email=fake.email(), password="")

    def test_email_exception_raised(self) -> None:
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password=fake.password())

    def test_superuser(self) -> None:
        super_user = User.objects.create_superuser(
            email=fake.email(), password=fake.password()
        )
        self.assertNotEqual(super_user.email, fake.email())

    def test_superuser_password_error(self) -> None:
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email=fake.email(), password="")

    def test_superuser_email_error(self) -> None:
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="", password=fake.password())

    def test_superuser_is_staff_error(self) -> None:
        user = User.objects.create_superuser(
            email=fake.email(),
            password=fake.password(),
        )
        self.assertTrue(user.is_staff)

    def test_superuser_error(self) -> None:
        user = User.objects.create_superuser(
            email=fake.email(),
            password=fake.password(),
        )
        self.assertTrue == user.is_admin

    def test_user_representation_is_email(self) -> None:
        user = User.objects.create_user(
            email=fake.email(), password=fake.password()
        )
        self.assertEqual(str(user), user.email)
