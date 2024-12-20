"""
Django settings for NeverNote project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
from os import getenv
import os
# from dotenv import load_dotenv
# from urllib.parse import urlparse
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p#cbl=qlxh#y-ds8vj(8tj=u659)a(ta#5)=$1wx%!pay==#7r'         # done by Abhijit to see if keeping it in other files work
# SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")          #Nah too much issues

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['10.0.2.2','127.0.0.1', '0.0.0.0','172.26.83.117' ,
                '*',                                                 #the '*' is a temporary measure to hellp while deploying, remember to fill in exact site and remove the all option    
                ]                   


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'module',
    'rest_framework',
    'api',
]

# EXTERNAL_APPS = [
#     'module',
#     'rest_framework',
#     'api',
    
# ]

# INSTALLED_APPS = INSTALLED_APPS + EXTERNAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'NeverNote.urls'

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

WSGI_APPLICATION = 'NeverNote.wsgi.application'

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://10.0.2.2:8000",
    "http://0.0.0.0:8000",
    "http://172.26.83.117:8000",
    # Add other origins if needed
]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# load_dotenv()
# tmpPostgres = urlparse(os.getenv("DATABASE_URL"))
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': tmpPostgres.path[1:],
#         'USER': tmpPostgres.username,
#         'PASSWORD': tmpPostgres.password,
#         'HOST': tmpPostgres.hostname,
#         'PORT': tmpPostgres.port,
#     }
# }

# following commented out to test deployment
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'NeverNote',
#         'USER': 'postgres',
#         'PASSWORD': 'admin',
#         'HOST': 'localhost',  # Set to 'localhost' if the database is on the same machine
#         'PORT': '5432',  # Default is '5432'
#     }
# }


# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.getenv('DATABASE_URL', 'postgres://postgres:admin@localhost:5432/NeverNote')
#     )
# }
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://nevernote_db_user:3EXqrSsebxs3SXaa3fd5ebxUTyu3qyL7@dpg-csiajsl6l47c73f6kgf0-a.oregon-postgres.render.com/nevernote_db'
    )
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    # Use Django's standard django.contrib.auth permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}