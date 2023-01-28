from .base import *

DEBUG = False
ALLOWED_HOSTS = ['jnbdrive.info','3.39.225.168', 'localhost', '127.0.0.1']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
db_port = os.getenv('DB_PORT')
db_host_adds = os.getenv('DB_HOST_ADDRESS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #'django.db.backends.sqlite3',
        'NAME': 'jnbdrive', #BASE_DIR / 'db.sqlite3',
        'USER': 'pajama',
        'PASSWORD': 'Gotobali1!',
        'HOST': db_host_adds,
        'PORT': db_port,
    }
}

STATIC_ROOT = './staticfiles'

SESSION_COOKIE_AGE = 7200
# SESSION_COOKIE_SECURE=True
# CSRF_COOKIE_SECURE=True
