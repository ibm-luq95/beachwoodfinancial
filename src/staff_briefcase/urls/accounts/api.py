# -*- coding: utf-8 -*-#

from rest_framework import routers

from staff_briefcase.views.accounts import StaffAccountsViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(
    r"staff-accounts-api", StaffAccountsViewSet, basename="staff-accounts-api-router"
)

urlpatterns = router.urls
