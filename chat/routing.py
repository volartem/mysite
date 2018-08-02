# chat/routing.py
from django.conf.urls import url

from . import chat_consumer
from . import users_consumer


websocket_urlpatterns = [
    url(r'^ws/chat/$', chat_consumer.ChatConsumer),
    url(r'^ws/users/$', users_consumer.UsersConsumer),
]
