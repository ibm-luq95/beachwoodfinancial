from .base import *

DEBUG = config("DEBUG", cast=bool)

ADMINS = [("Ibrahim Luqman", "ibm_luq995@outlook.com")]
MANAGERS = [("Ibrahim Luqman", "ibm_luq995@outlook.com")]


AUTH_PASSWORD_VALIDATORS = [
    {
        # Checks the similarity between the password and a set of attributes of the user.
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        "OPTIONS": {
            "user_attributes": ("email", "first_name", "last_name"),
            "max_similarity": 0.7,
        },
    },
    {
        # Checks whether the password meets a minimum length.
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 8,
        },
    },
    {
        # Checks whether the password occurs in a list of common passwords
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        # Checks whether the password isn’t entirely numeric
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Database configurations
DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", cast=str),
        "NAME": config("DB_NAME", cast=str),
        "USER": config("DB_USER", cast=str),
        "PASSWORD": config("DB_PASSWORD", cast=str),
        "HOST": config("DB_HOST", cast=str),
        "PORT": config("DB_PORT", cast=str),
        "OPTIONS": {"client_encoding": config("DB_CLIENT_ENCODING", cast=str)},
    }
}

# Django production deployment settings
CSRF_COOKIE_SECURE = config("CSRF_COOKIE_SECURE", cast=bool)
SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS", cast=bool)
SECURE_HSTS_INCLUDE_SUBDOMAINS = config("SECURE_HSTS_INCLUDE_SUBDOMAINS", cast=bool)
SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", cast=bool)
SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE", cast=bool)
SECURE_HSTS_PRELOAD = config("SECURE_HSTS_PRELOAD", cast=bool)
USE_X_FORWARDED_HOST = config("USE_X_FORWARDED_HOST", cast=bool)

# OWSP recommendation security configs
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
# SECURE_PROXY_SSL_HEADER = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
