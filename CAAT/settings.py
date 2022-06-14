import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-i=j9we7c8xx6w8uv$&3@n3pc#-0ko9xt@ah3bovn6(m6eq$l=i'


ALLOWED_HOSTS = ['caat0701.herokuapp.com','localhost','127.0.0.1','college-erp-0701.herokuapp.com']

DEBUG=True

CSRF_TRUSTED_ORIGINS = ['https://*.caat0701.herokuapp.com','https://*.127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Student.apps.StudentConfig',
    'Teacher.apps.TeacherConfig',
    'Home.apps.HomeConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CAAT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'CAAT.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'caat',
        'USER': 'postgres',
        'PASSWORD': 'Iloveu3000',
        'HOST': 'localhost'
    }
}
db_from_env=dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'
# STATIC_ROOT0=os.path.join(BASE_DIR,'static')
STATICFILES_DIRS=[
    BASE_DIR /'static',
]
STATIC_ROOT= BASE_DIR / 'asset'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
