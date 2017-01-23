from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Visitor(User):
    uid = models.BigIntegerField(blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.SlugField(max_length=255)
    access_token = models.SlugField(max_length=255)