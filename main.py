"""
Run the WSGI callable as a module-level 
variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import logging
import os

logging.info('1- in main.py')
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ung_www.settings")
#logging.info('DJANGO_SETTINGS_MODULE='+"ung_www.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
logging.info('2- DJANGO_SETTINGS_MODULE='+"settings")

logging.info('3- in main.py')
# app.yaml entry point
import django.core.handlers.wsgi
app = django.core.handlers.wsgi.WSGIHandler()

logging.info('4- get wsgi')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

logging.info('5- out of main.py')