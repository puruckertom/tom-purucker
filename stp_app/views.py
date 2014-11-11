from django.http import HttpResponse
from django.template.loader import render_to_string

import logging

logging.info('15- stp_app/views.py')

def home(request):
    logging.info('17- in home request')
    html = render_to_string('index.html')
    response = HttpResponse()
    response.write(html)
    return response

def hello_world(request):
    return HttpResponse("Hello, world.")

logging.info('16- done with stp_app/views.py')