"""
WSGI config for Project32.

This exposes the WSGI callable as a module-level variable named ``application``.
It's used by production servers like Gunicorn (see Dockerfile).
"""

import os
from django.core.wsgi import get_wsgi_application

# Default to production settings for WSGI; override via env if needed.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.environ.get(
    "DJANGO_SETTINGS_MODULE", "project32.settings.prod"
))

application = get_wsgi_application()
