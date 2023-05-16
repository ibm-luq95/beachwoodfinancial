"""
URL configuration for beach_wood_financial_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core.views import js_settings

static_and_media_path_urls = static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path("js-settings/", js_settings, name="js_settings"),
]

if settings.DEBUG:
    urlpatterns += static_and_media_path_urls
    # urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    # urlpatterns.append(
    #     path("request-logs/", include("request_viewer.urls")),
    # )
    urlpatterns.append(path("admin/doc/", include("django.contrib.admindocs.urls")))
    urlpatterns.append(path("admin/", admin.site.urls))
else:
    urlpatterns.append(path("secret/", admin.site.urls))
