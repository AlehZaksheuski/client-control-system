import django_heroku
import dj_database_url
from client_control_system.settings import *

DEBUG = False

django_heroku.settings(locals())
DATABASES['default'] = dj_database_url.config()
