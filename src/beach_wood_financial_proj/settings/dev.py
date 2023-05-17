import mimetypes

from .base import *

mimetypes.add_type("application/javascript", ".js", True)

DEBUG = config("DEBUG", cast=bool)

INSTALLED_APPS = INSTALLED_APPS + [
    "django.contrib.admindocs",
    "debug_toolbar",
    # "request_viewer",
]

MIDDLEWARE = MIDDLEWARE + [
    # "request_viewer.middleware.RequestViewerMiddleware",
    # "request_viewer.middleware.ExceptionMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
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
        "OPTIONS": {
            "read_default_file": "/opt/lampp/etc/my.cnf",
            "init_command": "SET default_storage_engine=INNODB",
        },
    }
}

# Set Cache Configurations

# Cache Redis
CACHES = {
    "default": {
        "BACKEND": config("CACHE_BACKEND_ENGINE", cast=str),
        "LOCATION": f"redis://:{config('REDIS_PASSWORD')}@{config('REDIS_HOST')}:{config('REDIS_PORT')}",
        "TIMEOUT": None,
    }
}
# Djagno Debug Toolbar
INTERNAL_IPS = config("INTERNAL_IPS", cast=Csv())
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


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

GRAPH_MODELS = {
    "all_applications": True,
    "group_models": True,
}

# django-request-viewer configs
REQUEST_VIEWER = {"LIVE_MONITORING": False, "WHITELISTED_PATH": []}

X_FRAME_OPTIONS = "SAMEORIGIN"
