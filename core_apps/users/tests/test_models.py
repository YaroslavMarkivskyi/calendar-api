"""
Tests for Django models.

This module contains test cases for verifying
the behavior of Django models,
including user creation, email normalization,
and the creation of recipe, tag, and ingredient models.

Dependencies:
- unittest.mock.patch
- decimal.Decimal
- django.test.TestCase
- django.contrib.auth.get_user_model
- core.models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test cases for Django models."""

    def test_create_user_with_email_successful(self):
        """
        Test that creating a new user with an email is successful.
        """
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Test that email addresses are normalized for new users.
        """
        sample_emails = [
            ["test1@EXAMPLE.COM", "test1@example.com"],
            ["Test2@EXAMPLE.COM", "Test2@example.com"],
            ["Test3@EXAMPLE.COM", "Test3@example.com"],
            ["Test4@EXAMPLE.COM", "Test4@example.com"],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """
        Test that creating a user without an email raises a ValueError.
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "test123")

    def test_create_superuser(self):
        """
        Test that creating a new superuser is successful.
        """
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "test123",
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
