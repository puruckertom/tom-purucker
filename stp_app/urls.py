from django.conf.urls.defaults import *
#from stp_app.views import home

import logging
logging.info('6- stp_app/urls.py')

urlpatterns = patterns('',
	(r'^home/$', 'stp_app.views.home'),
)

logging.info('7- made it')

#urlpatterns = patterns('',
#    url(URL 1, function_name 1, page_name 1),
#    . . .
#    url(URL n, function_name n, page_name n),
#)