import mimetypes
import os

from .base import *

mimetypes.add_type("application/javascript", ".js", True)

DEBUG = config("DEBUG", cast=bool)

INSTALLED_APPS = INSTALLED_APPS + [
    "django.contrib.admindocs",
    "debug_toolbar",
    "debugtools",
    "debug_permissions",
    "django_model_info.apps.DjangoModelInfoConfig",
    "silk",
    # "django_pdb",
    # "request_viewer",
]

# INSTALLED_APPS.insert(0, "django_pdb")

MIDDLEWARE = MIDDLEWARE + [
    # "request_viewer.middleware.RequestViewerMiddleware",
    # "request_viewer.middleware.ExceptionMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "debugtools.middleware.XViewMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
    "django_pdb.middleware.PdbMiddleware",
    "silk.middleware.SilkyMiddleware",
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
        "CONN_MAX_AGE": None,
        "OPTIONS": {"init_command": "SET default_storage_engine=INNODB"},
    }
}
# check if the code run locally or on the host
if config("WHEREAMI", cast=str) == "LOCAL":
    DATABASES["default"]["OPTIONS"].update({"read_default_file": "/opt/lampp/etc/my.cnf"})

TEMPLATES[0]["OPTIONS"]["builtins"].extend(
    ["debugtools.templatetags.debugtools_tags", "core.templatetags.development_tags"]
)

# DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True
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
    "debugtools.panels.ViewPanel",
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

GRAPH_MODELS = {"all_applications": True, "group_models": True}

# django-request-viewer configs
REQUEST_VIEWER = {"LIVE_MONITORING": False, "WHITELISTED_PATH": []}

X_FRAME_OPTIONS = "SAMEORIGIN"

# django-silk settings
SILKY_PYTHON_PROFILER = True
SILKY_PYTHON_PROFILER_BINARY = True
SILKY_META = True
# SILKY_ANALYZE_QUERIES = True
# SILKY_EXPLAIN_FLAGS = {'format':'JSON', 'costs': True}
SILKY_PERMISSIONS = lambda user: user.is_superuser
SILKY_AUTHENTICATION = True  # User must login
SILKY_AUTHORISATION = True  # User must have permissions
SILKY_PYTHON_PROFILER_EXTENDED_FILE_NAME = True
SILKY_PYTHON_PROFILER_RESULT_PATH = BASE_DIR / "media" / "profiles"

# Logging configs
# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "verbose": {
#             "format": "{levelname} {asctime} {module} {message}",
#             "style": "{",
#         },
#     },
#     "handlers": {
#         "console": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#             "formatter": "verbose",
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["console"],
#             "level": "INFO",
#         },
#         "bw_log": {
#             "handlers": ["console"],
#             "level": "DEBUG",
#         },
#     },
# }
