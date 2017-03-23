from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.postgres.fields import ArrayField


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
    # moderate = models.BooleanField(default=False)
    path = ArrayField(models.IntegerField(), null=True, blank=True)

    def __str__(self):
        return self.title


class Something(models.Model):
    method = models.CharField(max_length=7)
    path = models.CharField('Path', max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    status_code = models.IntegerField('Status code')
    ip = models.GenericIPAddressField()
    refer = models.SlugField(default='not_refer', null=True)

    def __str__(self):
        return '%s %s' % (self.method, self.ip)
