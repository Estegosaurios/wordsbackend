from wordsbackend.settings.base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wordsbackend',
        'USER': 'wordsbackend',
        'PASSWORD': 'wordsbackend',
        'HOST': 'db',
        'PORT': 5432,
    }
}
