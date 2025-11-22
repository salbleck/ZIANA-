import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Templates
TEMPLATE_DIR = BASE_DIR / 'templates'

# Static
STATIC_DIR = BASE_DIR / 'static'

# ⚠ MEDIA (Tidak bisa dipakai di Vercel — file tidak akan tersimpan)
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# =============================================================
# SECURITY & DEBUG
# =============================================================

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "development-secret-key")

DEBUG = os.environ.get("DEBUG", "True") == "True"

ALLOWED_HOSTS = ["*"]


# =============================================================
# INSTALLED APPS
# =============================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # your apps
    'quiz',
    'teacher',
    'student',

    # packages
    'widget_tweaks',
]


# =============================================================
# MIDDLEWARE
# =============================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'onlinequiz.urls'


# =============================================================
# TEMPLATES
# =============================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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


# =============================================================
# WSGI
# =============================================================

WSGI_APPLICATION = 'onlinequiz.wsgi.application'


# =============================================================
# DATABASE (Gunakan SQLite kalau local / Vercel dummy)
# =============================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =============================================================
# PASSWORD VALIDATION
# =============================================================

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


# =============================================================
# INTERNATIONALIZATION
# =============================================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# =============================================================
# STATIC FILES (Vercel Compatible)
# =============================================================

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = BASE_DIR / 'staticfiles'


# =============================================================
# LOGIN
# =============================================================

LOGIN_REDIRECT_URL = '/afterlogin'


# =============================================================
# EMAIL SETTINGS
# =============================================================

EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'zkldn3285@gmail.com'
EMAIL_HOST_PASSWORD = 'uwixxltxbgxhtvgw'
EMAIL_RECEIVING_USER = ['sitialfinahursalsabila@gmail.com']
