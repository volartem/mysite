from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Message(models.Model):
    author = models.ForeignKey(User, related_name='User_message', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)

    def as_dict(self):
        return {
            'author': self.author.username,
            'message': self.message,
            'date': self.timestamp.strftime('%Y-%m-%d %H:%M')
        }


class LoggedInUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='logged_in_user', on_delete=models.CASCADE)

    def as_dict(self):
        return {
            'username': self.user.username,
            'status': 'online'
        }
