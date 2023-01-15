from .base import *

ALLOWED_HOSTS = []
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
db_port = 3306
db_host_adds = '127.0.0.1'

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

