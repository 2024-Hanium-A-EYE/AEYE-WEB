# myapp/routing.py

from django.urls import re_path
from api.views.AEYE_WL_consumer import AEYE_WL_consumer

websocket_urlpatterns = [
    re_path(r'ws/web-websocket-log/$', AEYE_WL_consumer.as_asgi()),
]
