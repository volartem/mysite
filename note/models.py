from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Note(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextUploadingField(blank=True, default='')
    date_create = models.DateField(auto_now=True)
    rubric = models.CharField(max_length=255, default='Other')

    def __str__(self):
        return self.title


class Comment(models.Model):
    note = models.ForeignKey(Note, related_name='comments')
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='User', null=True)

    def __str__(self):
        return self.title
