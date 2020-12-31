"""
Django settings for netease project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import datetime
import logging
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "k$#)=xi(%g^jk#ii!&6kx42u*zps@2-^x3kt6wk-tn1tcwz=xv"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        "TIMEOUT": 300,
        "OPTIONS": {
            "MAX_ENTRIES": 300,
            "CULL_FREQUENCY": 3,
        },
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s] %(message)s"
        }
    },
    "filters": {},
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
        },
        "default": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "{}/home/log/{}.log".format(
                BASE_DIR, datetime.datetime.now().date()
            ),
            "maxBytes": 1024 * 1024 * 5,
            "formatter": "standard",
        },
        "error": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "{}/home/log/Error_{}.log".format(
                BASE_DIR, datetime.datetime.now().date()
            ),
            "maxBytes": 1024 * 1024 * 5,
            "formatter": "standard",
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "request_handler": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "{}/home/log/Request_{}.log".format(
                BASE_DIR, datetime.datetime.now().date()
            ),
            "maxBytes": 1024 * 1024 * 5,
            "formatter": "standard",
        },
        "scripts_handler": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "{}/home/log/Script_{}.log".format(
                BASE_DIR, datetime.datetime.now().date()
            ),
            "maxBytes": 1024 * 1024 * 5,
            "formatter": "standard",
        },
    },
    "loggers": {
        "django": {"handlers": ["console"], "level": "DEBUG", "propagate": False},
        "django.request": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "scripts": {
            "handlers": ["scripts_handler"],
            "level": "INFO",
            "propagate": False,
        },
        "console": {"handlers": ["console"], "level": "DEBUG", "propagate": True},
        # API/Views 模块的日志处理
        "views": {
            "handlers": ["default", "error"],
            "level": "DEBUG",
            "propagate": True,
        },
        "util": {"handlers": ["error"], "level": "ERROR", "propagate": True},
    },
}

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "api.apps.ApiConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # 'django.middleware.csrf.CsrfViewMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "netease.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "home/templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "netease.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"

MEDIA_URL = "/images/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


CELERY_IMPORTS = ("async_tasks.tasks",)
