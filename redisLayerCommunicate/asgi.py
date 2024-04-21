"""
ASGI config for redischannel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from redisApp import routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'redischannel.settings')

application = ProtocolTypeRouter({
    'https':get_asgi_application(),
    'websocket':URLRouter(routing.websocket_urlpatterns)
})
