"""
Django settings for beach_wood_financial_proj project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from importlib import import_module
from pathlib import Path
from decouple import Config, RepositoryEnv, Csv
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent  # Default BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_file_path = BASE_DIR / ".env" / ".env_dev"

config = Config(RepositoryEnv(env_file_path))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", cast=str)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    # "django.contrib.sites",  # TODO: enable it
    "django_extensions",
    "webpack_boilerplate",
    "django_components",
    "crispy_forms",
    "crispy_tailwind",
    "log_viewer",
    "maintenance_mode",
    "import_export",
    "django_filters",
    "rest_framework",
    "slippers",
    "widget_tweaks",
    "rangefilter",
    "core.apps.CoreConfig",
    "beach_wood_user.apps.BeachWoodUserConfig",
    "home.apps.HomeConfig",
    "bookkeeper.apps.BookkeeperConfig",
    "assistant.apps.AssistantConfig",
    "manager.apps.ManagerConfig",
    "dashboard.apps.DashboardConfig",
    "bw_ui_components.apps.BwUiComponentsConfig",
    "client_category.apps.ClientCategoryConfig",
]

MIDDLEWARE = [
    # "django.middleware.cache.UpdateCacheMiddleware",  # new for the cache
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django_session_timeout.middleware.SessionTimeoutMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "bookkeeper.middleware.CheckAllowedLoginMiddleware",   # TODO: Enable it
    "maintenance_mode.middleware.MaintenanceModeMiddleware",
    # "django.middleware.cache.FetchFromCacheMiddleware",  # new for the cache
]

ROOT_URLCONF = "beach_wood_financial_proj.urls"

UI_COMPONENTS_TEMPLATETAGS = [
    "core.templatetags.nospaces",
    "bw_ui_components.templatetags.inputs.label",
    "bw_ui_components.templatetags.inputs.button",
    "bw_ui_components.templatetags.inputs.input",
    "bw_ui_components.templatetags.inputs.select",
    "bw_ui_components.templatetags.inputs.radiobox",
    "bw_ui_components.templatetags.inputs.checkbox",
    "bw_ui_components.templatetags.inputs.file_input",
    "bw_ui_components.templatetags.elements.anchor",
    "bw_ui_components.templatetags.elements.icon",
    "bw_ui_components.templatetags.table_list.table",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
            BASE_DIR / "components",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # "django.template.context_processors.i18n",
                "core.context_processors.access_constants",
                "core.context_processors.access_css_classes_constants",
                "core.context_processors.access_constants_as_group",
                "maintenance_mode.context_processors.maintenance_mode",
            ],
            "builtins": [
                *UI_COMPONENTS_TEMPLATETAGS,
                "slippers.templatetags.slippers",
                "django_components.templatetags.component_tags",
            ],
        },
    },
]

WSGI_APPLICATION = "beach_wood_financial_proj.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 7,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Set login and logout urls
# LOGIN_REDIRECT_URL = "auth:login"  # The URL or named URL pattern where requests
# are redirected after login when the LoginView doesn’t get a next GET parameter.
LOGOUT_REDIRECT_URL = "home:landing"
LOGIN_URL = "auth:login"
LOGOUT_URL = "auth:logout"

# Set auth user model
AUTH_USER_MODEL = "beach_wood_user.BWUser"

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = config("LANGUAGE_CODE", cast=str)

TIME_ZONE = config("TIME_ZONE", cast=str)

USE_I18N = config("USE_I18N", cast=bool)

USE_TZ = config("USE_TZ", cast=bool)

LOCALE_PATHS = [
    BASE_DIR / "locale/",
]

LANGUAGES = (("en", "English"),)

# Django rest framework configs
REST_FRAMEWORK = {
    # "EXCEPTION_HANDLER": "core.errors.api_exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        # "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        # "rest_framework.parsers.FormParser",
    ],
    "DATETIME_FORMAT": "%Y-%m-%d",
}

# Django maintenance mode configs
MAINTENANCE_MODE_STATE_FILE_PATH = BASE_DIR / "maintenance_mode_state.txt"
# the template that will be shown by the maintenance-mode page
MAINTENANCE_MODE_TEMPLATE = "maintenance/503.html"

# the HTTP status code to send
# MAINTENANCE_MODE_STATUS_CODE = 404

# list of urls that will not be affected by the maintenance-mode
# urls will be used to compile regular expressions objects
MAINTENANCE_MODE_IGNORE_URLS = (r"^/manager", r"/logout", r"/")

# if True admin site will not be affected by the maintenance-mode page
MAINTENANCE_MODE_IGNORE_ADMIN_SITE = True

# if True the superuser will not see the maintenance-mode page
MAINTENANCE_MODE_IGNORE_SUPERUSER = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "frontend" / "build",
    BASE_DIR / "components",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media URLs
MEDIA_ROOT = BASE_DIR / "media"

MEDIA_URL = "media/"

# Whitenoise configs
STATICFILES_STORAGE = config("STATICFILES_STORAGE", cast=str)
WHITENOISE_MANIFEST_STRICT = config("WHITENOISE_MANIFEST_STRICT", cast=bool)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Use new password Scrypt algorithm
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.ScryptPasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# Crispy Configs
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

# Django session timeout configs
SESSION_COOKIE_AGE = config("SESSION_COOKIE_AGE", cast=int)
SESSION_EXPIRE_SECONDS = config("SESSION_EXPIRE_SECONDS", cast=int)  # 1 hour
SESSION_EXPIRE_AT_BROWSER_CLOSE = config(
    "SESSION_EXPIRE_AT_BROWSER_CLOSE", cast=bool
)  # Invalid session
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = config(
    "SESSION_EXPIRE_AFTER_LAST_ACTIVITY", cast=bool
)

SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 60  # group by minute

# Backup password
BACKUP_KEY = config("BACKUP_KEY", cast=str)
COMPRESS_LEVEL = config("COMPRESS_LEVEL", cast=int)

# ENCRYPT_KEY
ENCRYPT_KEY = bytes(config("ENCRYPT_KEY", cast=str), "ascii")

# Webpack configs
WEBPACK_LOADER = {
    # 'MANIFEST_FILE': BASE_DIR / "frontend/build/manifest.json",
    "MANIFEST_FILE": BASE_DIR
    / "frontend"
    / "build"
    / "manifest.json",
}

# Django logs configs
# Django log viewer package config
LOG_VIEWER_FILES_DIR = BASE_DIR / "logs"
LOG_VIEWER_PAGE_LENGTH = 25  # total log lines per-page
LOG_VIEWER_MAX_READ_LINES = 1000  # total log lines will be read
LOG_VIEWER_FILE_LIST_MAX_ITEMS_PER_PAGE = 25  # Max log files loaded in Datatable per page
LOG_VIEWER_PATTERNS = ["[INFO]", "[DEBUG]", "[WARNING]", "[ERROR]", "[CRITICAL]"]
LOG_VIEWER_EXCLUDE_TEXT_PATTERN = (
    None  # String regex expression to exclude the log from line
)
# Optionally you can set the next variables in order to customize the admin:
LOG_VIEWER_FILE_LIST_TITLE = "Log viewer"

# Django flash messages css classes
MESSAGE_TAGS = {
    messages.DEBUG: "bw-debug",
    messages.INFO: "bw-info",
    messages.SUCCESS: "bw-success",
    messages.WARNING: "bw-warning",
    messages.ERROR: "bw-error",
}

# check if cache enabled
if config("IS_CACHE_ENABLED", cast=bool) is True:
    CACHE_MIDDLEWARE_ALIAS = config(
        "CACHE_MIDDLEWARE_ALIAS", cast=str
    )  # which cache alias to use
    CACHE_MIDDLEWARE_SECONDS = config(
        "CACHE_MIDDLEWARE_SECONDS", cast=int
    )  # number of seconds to cache a page for (TTL)

    CACHE_MIDDLEWARE_KEY_PREFIX = config(
        "CACHE_MIDDLEWARE_KEY_PREFIX", cast=str
    )  # should be used if the cache is shared across multiple sites that
    # use the
    # same
    # Django instance
