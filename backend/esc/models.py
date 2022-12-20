from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# custom User model to allow email sign instead of user


class User(AbstractUser):
    email = models.EmailField("user email", max_length=240, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        # "username",
    ]

    def __str__(self):
        return str(self.email)


class User_Role(models.Model):
    role_name = models.CharField(max_length=15, unique=True)

    def __str__(self) -> str:
        return self.role_name


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.ForeignKey(User_Role, on_delete=models.CASCADE, default=1, null=True)
    avatar = models.ImageField(upload_to="media/avatars", null=True)
    phone_no = models.CharField(max_length=20, default=0)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        verbose_name = "Profile"
