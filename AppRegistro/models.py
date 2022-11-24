from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User


class Users(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)

