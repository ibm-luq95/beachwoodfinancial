# -*- coding: utf-8 -*-#

from rest_framework import routers

from staff_briefcase.views.notes import StaffNotesViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"staff-notes-api", StaffNotesViewSet, basename="staff-note-api-router")

urlpatterns = router.urls
