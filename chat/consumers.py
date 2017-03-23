from channels import Group
import json
from channels.auth import channel_session_user, channel_session_user_from_http
from .models import Message, LoggedInUser
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@channel_session_user_from_http
def ws_connect(message):
    print('ws_connect', message)
    messages = Message.objects.all()
    dict_message = [obj.as_dict() for obj in messages]
    message.reply_channel.send({"accept": True})
    Group('chat').add(message.reply_channel)
    if dict_message is not None:
        if message.user.username:
            text = json.dumps({
                'messages': dict_message

            })
            Group('chat').send({'text': text})
        else:
            text = json.dumps({
                'messages': dict_message

            })
            Group('chat').send({'text': text})


@channel_session_user
def ws_message(message):
    if message.user.is_authenticated and message.content['text'] is not None:
        new_message = Message.objects.create(
            author=message.user,
            message=message.content['text']
        )
        new_message.save()

        Group('chat').send({
            'text': json.dumps({
                'message': new_message.message,
                'author': new_message.author.username,
                'date': new_message.timestamp.strftime('%Y-%m-%d %H:%M')
            })
        })


@channel_session_user
def ws_disconnect(message):
    print('ws_disconnect', message)
    Group('chat').discard(message.reply_channel)


def users_connect(message):
    message.reply_channel.send({"accept": True})
    Group('users').add(message.reply_channel)
    filter_users()


def users_message():
    filter_users()


@receiver(post_save, sender=LoggedInUser)
@receiver(post_delete, sender=LoggedInUser)
def send_update(sender, **kwargs):
    filter_users()


def filter_users():
    users = LoggedInUser.objects.filter(user__is_superuser=False)
    dict_users = [obj.as_dict() for obj in users]
    Group('users').send({
        'text': json.dumps({
            'users': dict_users
        })
    })
