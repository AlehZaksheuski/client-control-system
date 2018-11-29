import django_heroku
import dj_database_url
from client_control_system.settings.base import *

DEBUG = False

DATABASES['default'] = dj_database_url.config()

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

django_heroku.settings(locals())


