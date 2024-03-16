# -*- coding: utf-8 -*-#

from rest_framework import routers

from staff_briefcase.views.documents import StaffDocumentsViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(
    r"staff-documents-api", StaffDocumentsViewSet, basename="staff-documents-api-router"
)

urlpatterns = router.urls
