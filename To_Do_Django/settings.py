"""
Django settings for To_Do_Django project.
Production-ready configuration for Railway
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


# ======================
# SECURITY
# ======================
SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-dev-key")
DEBUG = False

ALLOWED_HOSTS = [
    "to-dodjango-production.up.railway.app",
    ".up.railway.app",
    "localhost",
    "127.0.0.1",
]


# ======================
# APPLICATIONS
# ======================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "whitenoise.runserver_nostatic",
    "tasks",
]


# ======================
# MIDDLEWARE
# ======================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ======================
# URLS / WSGI
# ======================
ROOT_URLCONF = "To_Do_Django.urls"

WSGI_APPLICATION = "To_Do_Django.wsgi.application"


# ======================
# TEMPLATES
# ======================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "tasks" / "templates"],
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


# ======================
# DATABASE
# ======================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ======================
# PASSWORD VALIDATION
# ======================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ======================
# INTERNATIONALIZATION
# ======================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# ======================
# STATIC FILES
# ======================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"


# ======================
# AUTH REDIRECTS
# ======================
LOGIN_REDIRECT_URL = "task_list"
LOGOUT_REDIRECT_URL = "task_list"


# ======================
# DEFAULT PRIMARY KEY
# ======================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
CSRF_TRUSTED_ORIGINS = [
    "https://to-dodjango-production.up.railway.app",
]
