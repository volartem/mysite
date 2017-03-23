from channels.routing import route
from chat.consumers import ws_connect, ws_disconnect, ws_message, \
    users_connect, users_message


channel_routing = [
    route('websocket.connect', ws_connect, path=r"^/chat/$"),
    route('websocket.connect', users_connect, path=r"^/users/$"),
    route("websocket.receive", ws_message, path=r"^/chat/$"),
    route("websocket.receive", users_message, path=r"^/users/$"),
    route('websocket.disconnect', ws_disconnect, path=r"^/chat/$"),
]
