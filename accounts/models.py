from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
     def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

     def create_superuser(self, email, password, **kwargs):
        return self.create_user(email, password, is_staff=True, is_superuser=True, **kwargs)


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = None  # replaced by email

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    @property
    def token(self):
        pass

    def __str__(self):
        return self.email
