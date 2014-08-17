from django.http import HttpResponse

import logging

logging.info('7- stp_app/views.py')

def home(request):
	logging.info('5- stp_app/views.py')
    return HttpResponse("here I am")

def hello_world(request):
    return HttpResponse("Hello, world.")