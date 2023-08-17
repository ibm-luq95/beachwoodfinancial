# -*- coding: utf-8 -*-#

from rest_framework import routers

from client.views import ClientViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"client-api", ClientViewSet, basename="client-api-router")

urlpatterns = router.urls
