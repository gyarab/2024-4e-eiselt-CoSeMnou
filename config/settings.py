import os
from pathlib import Path

# cesta ke korenovemu adresari projektu
BASE_DIR = Path(__file__).resolve().parent.parent

# tajny klic pro zabezpeceni aplikace
SECRET_KEY = 'vygenerovany_tajny_klic'

# zapnuti ladiciho rezimu
DEBUG = True

# povolene domeny
ALLOWED_HOSTS = []

# nainstalovane aplikace vcetne custom aplikace frontend
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'frontend',
]

# middleware vrstvy zpracovavajici pozadavky a odpovedi
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# hlavni url konfigurace projektu
ROOT_URLCONF = 'config.urls'

# konfigurace sablon
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # slozka s vlastnimi sablonami
        'DIRS': [BASE_DIR / 'templates'],
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

# wsgi vstupni bod aplikace
WSGI_APPLICATION = 'config.wsgi.application'

# nastaveni databaze sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# validace hesel pro prihlaseni
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

# jazykova lokalizace a casove pasmo
LANGUAGE_CODE = 'cs'
TIME_ZONE = 'Europe/Prague'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# nastaveni statickych souboru
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'frontend/static']

# nastaveni pro nahravani medii
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# vychozi typ primarniho klice v databazi
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'