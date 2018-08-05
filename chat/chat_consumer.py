from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Message


class ChatConsumer(WebsocketConsumer):
    room_group_name = 'chat'

    def connect(self):
        messages = Message.objects.all()
        dict_message = [obj.as_dict() for obj in messages]
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        if dict_message is not None:
            text = dict_message
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': text
                }
            )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.scope["user"]
        if user.is_authenticated:
            new_message = Message.objects.create(
                author=user,
                message=message
            )
            new_message.save()

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': {
                        'message': new_message.message,
                        'author': new_message.author.username,
                        'date': new_message.timestamp.strftime('%Y-%m-%d %H:%M')
                    }
                }
            )

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'messages': message
        }))
