"""
WSGI config for calltospeakers project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import os
from dj_static import Cling

ENVIRONMENT = os.getenv('ENVIRONMENT')

if ENVIRONMENT == 'PRODUCTION':
    settings = 'production'
else:
    settings = 'development'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calltospeakers.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', settings.title())

from configurations.wsgi import get_wsgi_application

application = Cling(get_wsgi_application())
