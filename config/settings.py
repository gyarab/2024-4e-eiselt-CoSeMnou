import os
from pathlib import Path

# BASE_DIR: Cesta ke kořenovému adresáři projektu
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY: Tajný klíč pro zabezpečení. Tento klíč by měl být dobře chráněný.
SECRET_KEY = 'vygenerovany_tajny_klic'

# DEBUG: Nastavení ladění. Ve vývojovém prostředí nastavte na True. Na produkci na False.
DEBUG = True

# ALLOWED_HOSTS: Povolené hostitelské adresy, na kterých může být aplikace spuštěna.
ALLOWED_HOSTS = []

# INSTALLED_APPS: Aplikace nainstalované v projektu
INSTALLED_APPS = [
    'django.contrib.admin',      # Administrační rozhraní
    'django.contrib.auth',       # Autentizace
    'django.contrib.contenttypes', # Typy obsahu
    'django.contrib.sessions',   # Správa uživatelských relací
    'django.contrib.messages',   # Systém zpráv
    'django.contrib.staticfiles', # Správa statických souborů
    'frontend',                  # Vaše vlastní aplikace
]

# MIDDLEWARE: Middleware komponenty, které zpracovávají požadavky a odpovědi
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT_URLCONF: Kořenová konfigurace URL pro projekt
ROOT_URLCONF = 'config.urls'

# TEMPLATES: Nastavení pro šablony (templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Kořenový adresář pro šablony
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

# WSGI_APPLICATION: Cesta k WSGI aplikaci, používaná pro nasazení na server
WSGI_APPLICATION = 'config.wsgi.application'

# DATABASES: Nastavení databáze
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Typ databáze (SQLite je výchozí)
        'NAME': BASE_DIR / 'db.sqlite3',         # Cesta k databázovému souboru
    }
}

# AUTH_PASSWORD_VALIDATORS: Validátory hesel
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

# LANGUAGE_CODE: Jazyk pro projekt
LANGUAGE_CODE = 'cs'

# TIME_ZONE: Časová zóna
TIME_ZONE = 'Europe/Prague'

# USE_I18N, USE_L10N, USE_TZ: Nastavení pro mezinárodní formátování a časové zóny
USE_I18N = True
USE_L10N = True
USE_TZ = True

# STATIC_URL: URL pro statické soubory
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'frontend/static']

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'



# DEFAULT_AUTO_FIELD: Výchozí typ primárního klíče pro modely
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
