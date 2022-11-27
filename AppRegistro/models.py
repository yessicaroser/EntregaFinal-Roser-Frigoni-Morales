from django.db import models
#from django.utils import timezone
#from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User


class Users(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(default='default.jpg', upload_to='images/profile')
    website_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

