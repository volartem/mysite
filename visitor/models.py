from django.db import models
from django.contrib.auth.models import User
from social_django.models import AbstractUserSocialAuth, UserSocialAuth


class Visitor(User):
    uid = models.CharField(max_length=255, blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.SlugField(max_length=255, default='')
    access_token = models.SlugField(max_length=255, default='')
