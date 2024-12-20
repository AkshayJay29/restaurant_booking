"""
WSGI config for restaurant_booking project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'restaurant_booking' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_booking.settings')

application = get_wsgi_application()
