"""
ASGI config for codeclause_chatapplication project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from chat_app.routing import websocket_urlpattern

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeclause_chatapplication.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),  
    'websocket':AuthMiddlewareStack(URLRouter(websocket_urlpattern))
})
