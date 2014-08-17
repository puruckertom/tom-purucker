from django.http import HttpResponse
from django.template.loader import render_to_string

import logging

logging.info('10- in ung_www/views.py')

def home(request):
	html = render_to_string('index.html')
	response = HttpResponse()
	response.write(html)
	return response

logging.info('11- out of ung_www/views.py')