"""
Database models for the application.

This module defines the database models for the application,
including user management, recipes, tags, and ingredients.
It also includes custom file path generation for recipe images.

Dependencies:
- uuid
- os
- django.conf.settings
- django.db.models
- django.contrib.auth.models.AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """
    Manager for handling user operations.

    Provides methods to create regular users and superusers.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a new user with an email address.

        Args:
            email (str): The email address of the user.
            password (str, optional): The password for the user.
            **extra_fields: Additional fields for the user.

        Returns:
            User: The created user instance.
        """
        if not email:
            raise ValueError("Users must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Create and return a new superuser with admin privileges.

        Args:
            email (str): The email address of the superuser.
            password (str): The password for the superuser.

        Returns:
            User: The created superuser instance.
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model representing a user in the system.

    Inherits from AbstractBaseUser and PermissionsMixin
    to provide user authentication and permission features.
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
