"""
Django settings for settings project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import environ
env = environ.Env()
environ.Env.read_env()



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env('SECRET_KEY')
# SECRET_KEY = env("SECRET_KEY")
SECRET_KEY='django-insecure-bxw2f&05ww(%i9*=3ivg)mg629(^8vuh9#96e#x10hgx@%%b5a'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'multiselectfield',
    'rest_framework',
    'django_nose',
    'accounts',
    'movieCollection',
    'movie',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'accounts.middleware.RequestCounterMiddleware'
]

ROOT_URLCONF = 'settings.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'
AUTH_USER_MODEL = 'accounts.User'

from settings.m_environ import testcases_db #,MOVIE_DB,MOVIE_DB_READ

if not testcases_db:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env("DB_NAME"),
            'USER': env("DB_USER"),
            'PASSWORD': env("DB_PASSWORD"),
            'HOST': env("DB_HOST"),
            'PORT': env("DB_PORT"),
        },
        'replica': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env("DB_NAME"),
            'USER': env("DB_USER"),
            'PASSWORD': env("DB_PASSWORD"),
            'HOST': env("DB_HOST"),
            'PORT': env("DB_PORT"),
        }
    }
# else:
#     DATABASES = {"default": MOVIE_DB,
#                  "replica": MOVIE_DB_READ}
#     DATABASES["default"]["ATOMIC_REQUESTS"] = False
#     DATABASES["default"]["ENGINE"] = "django.db.backends.postgresql_psycopg2"
#     DATABASES["default"]["CONN_MAX_AGE"] = 60

#     DATABASES["replica"]["ATOMIC_REQUESTS"] = False
#     DATABASES["replica"]["ENGINE"] = "django.db.backends.postgresql_psycopg2"
#     DATABASES["replica"]["CONN_MAX_AGE"] = 60

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=300),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    # 'AUTH_HEADER_TYPES': ('jwt',),
    # 'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    # 'USER_ID_FIELD': 'username',
    # 'USER_ID_CLAIM': 'user_id'  
}

# TEST_RUNNER = "settings.tests.TestRunner"

# AUTHENTICATION_BACKENDS = ('accounts.custom_auth.EmailBackend',)
############credy api keys##############
# CREDY_USERNAME = env('CREDY_USERNAME')
# CREDY_PASSWORD = env('CREDY_PASSWORD')
CREDY_USERNAME='iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0'
CREDY_PASSWORD='Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'