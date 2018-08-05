from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import LoggedInUser
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from channels.consumer import get_channel_layer


class UsersConsumer(WebsocketConsumer):
    room_group_name = 'users'
    channel_layer = get_channel_layer()

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send_loggined_users()

    @classmethod
    def send_loggined_users(cls):
        users = LoggedInUser.objects.all()
        dict_users = list(map(lambda obj: obj.as_dict(), users))
        async_to_sync(cls.channel_layer.group_send)(
            cls.room_group_name,
            {
                'type': 'chat_message',
                'message': dict_users
            }
        )

    @receiver([user_logged_in, user_logged_out])
    def send_update(sender, **kwargs):
        UsersConsumer.send_loggined_users()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'users': message
        }))
