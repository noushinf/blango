from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.apps import apps
from django.contrib import auth
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.db import models
from django.db.models.manager import EmptyManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# from .validators import UnicodeUsernameValidator


class BlangoUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must haveis_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must haveis_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True, )
    objects = BlangoUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class B(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name="profile")
