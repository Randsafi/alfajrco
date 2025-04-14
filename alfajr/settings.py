from pathlib import Path
import os
import dj_database_url  # type: ignore

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-98hdrh!*m3vxadau)bhn-*$@2$w@6v(fd0eim71qy$5@qu&ab='

DEBUG = False


ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://alfajrco.up.railway.app']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myalfajr',
    'whitenoise.runserver_nostatic', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # تأكد من إضافة WhiteNoise
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ROOT_URLCONF = 'alfajr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'alfajr.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # استخدام SQLite
        'NAME': BASE_DIR / 'db.sqlite3',  # قاعدة بيانات SQLite
    },
    #'mysql_db': {
    #    'ENGINE': 'django.db.backends.mysql',  # استخدام MySQL
    #    'NAME': 'alfajr',
    #    'USER': 'root',
    #    'PASSWORD': 'r80750497',
    #    'HOST': 'localhost',
    #    'PORT': '3306',
    #},

    'postgole': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )

    
}


   


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'alfajr/static')  # هذا هو المجلد الذي يحتوي على ملفات CSS و JS
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # المجلد الذي سيتم فيه جمع الملفات الستاتيكية

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
