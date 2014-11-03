from django.conf.urls import patterns, include, url
#from stp_app.views import home

import logging
logging.info('13- in ung_www/urls.py')

urlpatterns = patterns('',
	(r'^$', 'stp_app.views.home'),
)

logging.info('14- out of ung_www/urls.py')

#urlpatterns = patterns('',
#    url(URL 1, function_name 1, page_name 1),
#    . . .
#    url(URL n, function_name n, page_name n),
#)