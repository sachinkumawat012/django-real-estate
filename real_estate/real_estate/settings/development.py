from .base import *

DATABASES = {
    'default': {
        'ENGINE': env('PG_ENGINE'),
        'NAME': env('PG_NAME'),
        'USER': env('PG_USER'),
        'PASSWORD': env('PG_PASSWORD'),
        'HOST': env('PG_HOST'),
        'PORT': env('PG_PORT')
    }
}