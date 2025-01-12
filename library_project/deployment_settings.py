import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR

ALLOWED_hosts = [os.environ.get('RENDER_EXTERNAL_HOSTNAME')] 
CSRF_TRUSTED_ORIGINS = ['HTTPS://' +os.environ.get('RENDER_EXTERNAL_HOSTNAME')]
DEBUG = False
SECRET_KEY = os.environ.get('SEECRET_KEY')
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#CORS_ALLOWED_ORIGINS = [
# 'http://localhost:5173'
# ]
STORAGES = {
    "default":{
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles":{
        "BACKEND": "Whitenoise.storage.CompressedStaticFileStorage",

    },
}
DATABASES = {
    'default': dj_database_url.config(
        default = os.environ['DARABASE_URL'],
        conn_max_age = 600
    )
}