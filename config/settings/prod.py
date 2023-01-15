from .base import *

DEBUG = False
ALLOWED_HOSTS = ['192.168.0.102']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
db_port = os.getenv('DB_PORT')
db_host_adds = os.getenv('DB_HOST_ADDRESS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #'django.db.backends.sqlite3',
        'NAME': 'TEST_DB3', #BASE_DIR / 'db.sqlite3',
        'USER': 'jnb',
        'PASSWORD': 'jnbdrive-0922',
        'HOST': db_host_adds,
        'PORT': db_port,
    }
}

SESSION_COOKIE_AGE = 7200
# SESSION_COOKIE_SECURE=True
# CSRF_COOKIE_SECURE=True
