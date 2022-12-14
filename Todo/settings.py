import os

from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR_2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True



# SECURITY WARNING: don't run with debug turned on in production!


ALLOWED_HOSTS = ['p-task.up.railway.app', '127.0.0.1',]

CSRF_TRUSTED_ORIGINS = ['https://p-task.up.railway.app' , ]

APP_ENVIRONMENT = os.getenv('APP_ENVIRONMENT')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'task',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Todo.urls'
AUTH_USER_MODEL = 'task.CustomUser'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'Todo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if APP_ENVIRONMENT == 'Production':

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': os.getenv('PGHOST'),
            'PORT': os.getenv('PGPORT'),
            'NAME': os.getenv('PGDATABASE'),
            'USER': os.getenv('PGUSER'),
            'PASSWORD': os.getenv('PGPASSWORD'),

        },
    }
else:

    DATABASES = {
        'default': {
            'ENGINE': os.getenv('DB_ENGINE'),
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': '127.0.0.1',
            'PORT': '5432',
        },

    }



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

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR_2, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = 'mediafiles/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGOUT_REDIRECT_URL = 'home.html'

LOGIN_URL = 'login_page'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('APP_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('APP_EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True