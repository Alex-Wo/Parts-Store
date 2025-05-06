import os
from pathlib import Path

from django.conf.global_settings import MEDIA_URL
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG'))

# Hosts

ALLOWED_HOSTS = (os.getenv('ALLOWED_HOSTS'))

# Email verifications

DOMAIN_NAME = (os.getenv('DOMAIN_NAME'))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.vk',
    'debug_toolbar',

    'products',
    'orders',
    'users',
]

# Middleware

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'store.urls'

# Templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'products.context_processors.baskets',
            ],
        },
    },
]

WSGI_APPLICATION = 'store.wsgi.application'

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

# Caches

CACHES = {
    'default': {
        'BACKEND': (os.getenv('BACKEND')),
        'LOCATION': (os.getenv('LOCATION')),
    }
}

# Databases

DATABASES = {
    'default': {
        'ENGINE': (os.getenv('ENGINE')),
        'NAME': (os.getenv('NAME')),
        'USER': (os.getenv('USER')),
        'PASSWORD': (os.getenv('PASSWORD')),
        'HOST': (os.getenv('HOST')),
        'PORT': (os.getenv('PORT')),
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization

LANGUAGE_CODE = (os.getenv('LANGUAGE_CODE'))

TIME_ZONE = (os.getenv('TIME_ZONE'))

USE_I18N = (os.getenv('USE_I18N'))

USE_TZ = (os.getenv('USE_TZ'))

# Static files (CSS, JavaScript, Images)

STATIC_URL = (os.getenv('STATIC_URL'))
STATICFILES_DIRS = (os.getenv('STATICFILES_DIRS'))

MEDIA_URL = (os.getenv('MEDIA_URL'))
MEDIA_ROOT = (os.getenv('MEDIA_ROOT'))

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Users

AUTH_USER_MODEL = (os.getenv('AUTH_USER_MODEL'))
LOGIN_URL = (os.getenv('LOGIN_URL'))
LOGIN_REDIRECT_URL = (os.getenv('LOGIN_REDIRECT_URL'))
LOGOUT_REDIRECT_URL = (os.getenv('LOGOUT_REDIRECT_URL'))

# Sending emails

EMAIL_HOST = (os.getenv('EMAIL_HOST'))
EMAIL_PORT = (os.getenv('EMAIL_PORT'))
EMAIL_HOST_USER = (os.getenv('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD = (os.getenv('EMAIL_HOST_PASSWORD'))
EMAIL_USE_SSL = (os.getenv('EMAIL_USE_SSL'))

# Sending emails in console

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# OAuth

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = (os.getenv('SITE_ID'))

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}

# Celery

CELERY_BROKER_URL = (os.getenv('CELERY_BROKER_URL'))
CELERY_RESULT_BACKEND = (os.getenv('CELERY_RESULT_BACKEND'))

# Stripe

STRIPE_PUBLIC_KEY = (os.getenv('STRIPE_PUBLIC_KEY'))
STRIPE_SECRET_KEY = (os.getenv('STRIPE_SECRET_KEY'))
STRIPE_API_VERSION = (os.getenv('STRIPE_API_VERSION'))
STRIPE_WEBHOOK_SECRET = (os.getenv('STRIPE_WEBHOOK_SECRET'))
