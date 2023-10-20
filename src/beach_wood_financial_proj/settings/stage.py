from .base import *
import mimetypes

# SITE_NAME = "dev.beachwoodfinancial.com"

# ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=str).split(",")

DEBUG = config("DEBUG", cast=bool)

INSTALLED_APPS = INSTALLED_APPS + ["debug_toolbar", "request_viewer"]

MIDDLEWARE = MIDDLEWARE + ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# Database configurations
DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", cast=str),
        "NAME": config("DB_NAME", cast=str),
        "USER": config("DB_USER", cast=str),
        "PASSWORD": config("DB_PASSWORD", cast=str),
        "HOST": config("DB_HOST", cast=str),
        "PORT": config("DB_PORT", cast=str),
        "OPTIONS": {
            # "read_default_file": "/opt/lampp/etc/my.cnf",
            "init_command": "SET default_storage_engine=INNODB"
        },
    }
}

# Djagno Debug Toolbar
INTERNAL_IPS = config("INTERNAL_IPS", cast=str).split(", ")
DISABLE_PANELS = {}

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]

SHOW_COLLAPSED = True


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": show_toolbar}

mimetypes.add_type("application/javascript", ".js", True)

# Django production deployment settings
# CSRF_COOKIE_SECURE = config("CSRF_COOKIE_SECURE", cast=bool)
# SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS", cast=bool)
# SECURE_HSTS_INCLUDE_SUBDOMAINS = config("SECURE_HSTS_INCLUDE_SUBDOMAINS", cast=bool)
# SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", cast=bool)
# SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE", cast=bool)
# SECURE_HSTS_PRELOAD = config("SECURE_HSTS_PRELOAD", cast=bool)
# USE_X_FORWARDED_HOST = config("USE_X_FORWARDED_HOST", cast=bool)
