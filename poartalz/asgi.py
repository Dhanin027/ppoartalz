import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poartalz.settings')

# Standard Django ASGI application
application = get_asgi_application()

# Alias for Vercel compatibility
