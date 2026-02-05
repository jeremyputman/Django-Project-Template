# Django Imports
from pathlib import Path

# Application Imports
from apps.core.functions import get_secret_data

# Third party libraries
from decouple import config, Csv
from loguru import logger

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Configure KeyVault Settings
KEYVAULT_NAME = config("KEYVAULT_NAME")
KEYVAULT_ENABLED = config("KEYVAULT_ENABLED", default=False, cast=bool)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret_data('SECRET_KEY')

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'unfold',
    'unfold.contrib.import_export',
    'django_extensions',
    'import_export',
    'allauth',
    'allauth.account',   
    'allauth.socialaccount',
    'allauth.socialaccount.providers.saml',
    'auditlog',
    'tailwind',
    'theme',
]

LOCAL_APPS = [
    'apps.core',
    'apps.users',
]

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS

# Auth
AUTH_USER_MODEL = 'users.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'apps.core.middleware.LoguruContextMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
]

ROOT_URLCONF = '{{ project_name }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Toronto"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "../static",
]

# Media files such as uploads
MEDIA_ROOT = BASE_DIR / "../media"
MEDIA_URL = "/media/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Tailwind CSS Settings
TAILWIND_APP_NAME = "theme"

# Django Unfold Settings
from {{ project_name }}.settings.django_unfold import *
# Logging Settings
from {{ project_name }}.settings.logs import * # type: ignore
# SAML Settings
from {{ project_name }}.settings.saml import *

