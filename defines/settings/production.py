from .common import *
import environ
from django.core.management.commands.runserver import Command as runserver

runserver.default_port = 8002
ROOT_URLCONF = 'defines.urls.production'
COMPRESS_OFFLINE = True

MIDDLEWARE.insert(1,'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# info's read of platform in deploy
env = environ.Env()

DEBUG = env.bool('DEBUG', False)
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    'default': env.db(),
}
