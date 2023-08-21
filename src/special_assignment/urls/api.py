# -*- coding: utf-8 -*-#

from rest_framework import routers

from special_assignment.views import SpecialAssignmentViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(
    r"special-assignment-api",
    SpecialAssignmentViewSet,
    basename="special-assignment-api-router",
)

urlpatterns = router.urls
