"""
Django settings.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
import logging
logging.info('5- in ung_www/settings.py')

# Define ENVIRONMENTAL VARIABLES for project (replaces the app.yaml)
os.environ.update({
    # 'UBERTOOL_REST_SERVER': 'http://54.83.18.251:7777',
})

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = BASE_DIR

logging.info('BASE_DIR='+BASE_DIR)
logging.info('PROJECT_ROOT='+PROJECT_ROOT)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z3b!t&^1@2_vr6v737l&n+*5=3i1yt7$0f5e6kc$d*rqt@5kmg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# APPEND_SLASH = False

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates').replace('\\','/'),
)

logging.info('TEMPLATE_DIRS='+str(tuple(TEMPLATE_DIRS)))

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

INSTALLED_APPS = (
    # other stuff here,
#   'django.contrib.admin',
#    'django.contrib.comments',
#    'tagging',
#    'mptt',
#    'zinnia',
#    'appengine_toolkit
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
     'django.contrib.sessions',
#    'django.contrib.messages',
     'django.contrib.staticfiles',
     'stp_app'
)

MIDDLEWARE_CLASSES = (
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ung_www.urls'
logging.info('ROOT_URLCONF='+ROOT_URLCONF)

WSGI_APPLICATION = 'wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}

# Setups databse-less test runner (Only needed for running test)
TEST_RUNNER = 'testing.DatabaselessTestRunner'

# CACHE Setup - required to run Django "sessions" without a database

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake'
#     }
# }
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

logging.info('STATICFILES_DIRS='+str(tuple(STATICFILES_DIRS)))

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATIC_URL = '/static/'

print 'BASE_DIR = %s' %BASE_DIR
print 'PROJECT_ROOT = %s' %PROJECT_ROOT

logging.info('7 out of- ung_www/settings.py')

