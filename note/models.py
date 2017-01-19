from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=16)
    text = models.TextField()
    date_create = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    note = models.ForeignKey(Note, related_name='comments')
    title = models.CharField(max_length=16)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='User', null=True)

    def __str__(self):
        return self.title
