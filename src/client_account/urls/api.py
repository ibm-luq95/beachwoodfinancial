# -*- coding: utf-8 -*-#

from rest_framework import routers

from client_account.views import ClientAccountViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(
    r"client-accounts-api", ClientAccountViewSet, basename="client-account-api-router"
)

urlpatterns = router.urls
