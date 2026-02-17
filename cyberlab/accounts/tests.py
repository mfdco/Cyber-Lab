from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

#run this to test account ➜ .venv/bin/python3 cyberlab/manage.py test accounts -v 2
class AuthTests(TestCase):
    def test_signup(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "connor1",
                "email": "connor1@example.com",
                "password1": "password",
                "password2": "password",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username="connor1").exists())

    def test_login(self):
        User.objects.create_user(
            username="connor2",
            email="connor2@example.com",
            password="password",
        )
        response = self.client.post(
            reverse("login"),
            {"username": "connor2", "password": "password"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("account"))

    def test_account_needs_login(self):
        response = self.client.get(reverse("account"))
        self.assertEqual(response.status_code, 401)

    def test_account_data(self):
        user = User.objects.create_user(
            username="connor3",
            email="connor3@example.com",
            password="password",
        )
        self.client.force_login(user)

        response = self.client.get(reverse("account"))

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["username"], "connor3")
        self.assertEqual(data["email"], "connor3@example.com")
