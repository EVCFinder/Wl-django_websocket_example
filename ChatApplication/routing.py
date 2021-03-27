# ChatApplication/routing.py
from django.urls import re_path,path,include
from chat.routing import websocket_urlpatterns as chat_web_url
from ChatAsync.routing import websocket_urlpatterns as chat_a_web_url
from RandomIntegers.routing import websocket_urlpatterns as randomint_web_url
from AsyncRandomIntegers.routing import websocket_urlpatterns as randomint_a_web_url
from testOCPP.routing import websocket_urlpatterns as ocpp_web_url

from channels.routing import URLRouter

websocket_urlpatterns = [
    #path('ws/chat/',include('chat.routing.websocket_urlpatterns')),
    path('ws/chat/',URLRouter(chat_web_url)),
    path('ws/async/chat/',URLRouter(chat_a_web_url)),
    path('ws/randomint/',URLRouter(randomint_web_url)),
    path('ws/async/randomint/',URLRouter(randomint_web_url)),
    path('ws/testocpp/',URLRouter(ocpp_web_url)),
]