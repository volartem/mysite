from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=16)
    text = models.TextField()
    date_create = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    note = models.OneToOneField(Note)
    theme = models.CharField(max_length=16)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.theme
