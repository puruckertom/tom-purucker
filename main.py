"""
Run the WSGI callable as a module-level 
variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import logging
logging.info('1- in main.py')

# app.yaml entry point
import django.core.handlers.wsgi
app = django.core.handlers.wsgi.WSGIHandler()

logging.info('2- set environ')
import os
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ung_www.settings")
#logging.info('DJANGO_SETTINGS_MODULE='+"ung_www.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
logging.info('DJANGO_SETTINGS_MODULE='+"settings")

logging.info('3- get wsgi')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

logging.info('4- out of main.py')