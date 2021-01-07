"""
Django settings for bookthird project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3&*ts_c8l7tr=_wp(o9axw(ofrmz(ld3e4*4h)v^k5+ezz1^#6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop.apps.ShopConfig',
    'debug_toolbar',
    "cart.apps.CartConfig",
    "orders.apps.OrdersConfig",
    "django_celery_results",
    "payments.apps.PaymentsConfig",
    'coupon.apps.CouponConfig',
    'rosetta'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookthird.urls'

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
                'cart.context_processor.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'bookthird.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/
from django.utils.translation import gettext_lazy as _
LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
    ('hi', _('Hindi')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)
    

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'statics')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'statics/media/')
STATIC_CSS_DIR = os.path.join(STATIC_ROOT, 'css/')
# Debug Toolbar
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]


CART_SESSION_ID = 'cart'

# SMPT server setting
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'saiyedafzal0@gmail.com'
EMAIL_HOST_PASSWORD = '27021992Afzal'


# CELERY SETTINGS
CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = 'django-cache'


#BRAINTREE Settings
# Braintree settings
BRAINTREE_MERCHANT_ID = 'hbtcyt5cdy3xnz52' # Merchant ID
BRAINTREE_PUBLIC_KEY = 'c56hm8mwwc7fycm5' # Public Key
BRAINTREE_PRIVATE_KEY = 'baf31926b310f5cb909ca2bf0d7cd308' # Private key
import braintree
BRAINTREE_CONF = braintree.Configuration(
 braintree.Environment.Sandbox,
 BRAINTREE_MERCHANT_ID,
 BRAINTREE_PUBLIC_KEY,
 BRAINTREE_PRIVATE_KEY
)


# Strip Keys

STRIPE_PUBLIC_KEY = "pk_test_51I1ZLoILK0fYUsKSJKvf4Jzqf30swSnovxmteNo1VdBS8Q6NOoGc2yjOy9Rd8GvmCy1g82Aoy89B28KcXogF4pKQ00rVrybnP2"
STRIPE_SECRET_KEY = "sk_test_51I1ZLoILK0fYUsKSdLk82LoNbX0RCuaQPbXF9jFdbtoAjWpp3QlBuOgbH1k9iDtS8EkmXrQaqb1GDgClAYGk4m0600eT6QIBDZ"

# Redis SERVER

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1