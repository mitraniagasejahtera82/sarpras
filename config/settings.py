from pathlib import Path
import os
import dj_database_url
# =====================================
# BASE DIRECTORY
# =====================================
BASE_DIR = Path(__file__).resolve().parent.parent


# =====================================
# SECURITY
# =====================================
SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS",
    "sarpras.onrender.com"
).split(",")

CSRF_TRUSTED_ORIGINS = [
    "https://sarpras.onrender.com"
]

# =====================================
# APPLICATION DEFINITION
# =====================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # app utama
    'sarpras',
    
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # pindah ke sini

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # =====================================
        # TEMPLATE DIR
        # =====================================
        # agar Django bisa baca templates global
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


WSGI_APPLICATION = 'config.wsgi.application'

# =====================================
# DATABASE
# =====================================
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3')
    )
}


# =====================================
# PASSWORD VALIDATION
# =====================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# =====================================
# INTERNATIONALIZATION
# =====================================
LANGUAGE_CODE = 'id'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True
USE_TZ = True


# =====================================
# STATIC FILES (CSS, JS)
# =====================================
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# =====================================
# MEDIA FILES (UPLOAD GAMBAR)
# =====================================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# =====================================
# DEFAULT PRIMARY KEY
# =====================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
