import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PUBLIC_DIR = os.path.join(BASE_DIR, 'public')

# SECURITY WARNING: keep the secret key used in production secret!
# Generate a fresh one with `pwgen -s 60 1`
SECRET_KEY = '7_u_8k7n%vf0hxdhib!-urj#0*4mb7n0co)b!)i#7q@gq+hxa4'  # FIXME

DEBUG = True  # FIXME set to False for production

ALLOWED_HOSTS = []  # FIXME

# Database — will not be intensely used
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'en-us'  # FIXME
TIME_ZONE = 'UTC'  # FIXME
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PUBLIC_DIR, 'static')

PICTURES_URL = '/pictures/'
PICTURES_ROOT = os.path.join(PUBLIC_DIR, 'pictures')  # FIXME
