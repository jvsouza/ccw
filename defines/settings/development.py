from .common import *
from django.core.management.commands.runserver import Command as runserver

runserver.default_port = 8001
DEBUG = True
COMPRESS_OFFLINE = False
INSTALLED_APPS  +=  ['debug_toolbar',]
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '[::1]']
ROOT_URLCONF = 'defines.urls.development'
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
