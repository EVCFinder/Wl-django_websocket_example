# chat/routing.py
from django.urls import re_path,path


from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
# ]
#  path('<str:room_name>/',view=views.room,name='room'),

websocket_urlpatterns = [
    path('<str:room_name>/',consumers.ChatConsumer.as_asgi()),
]