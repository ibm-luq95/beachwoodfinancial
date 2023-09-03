# -*- coding: utf-8 -*-#
from django.urls import path

from beach_wood_user.views import StaffMemberDetailsView, UpdateStaffPermissionsApiView

app_name = "staff"

urlpatterns = [
    path("<uuid:pk>/", StaffMemberDetailsView.as_view(), name="member-details"),
    path(
        "api/update-permissions/",
        UpdateStaffPermissionsApiView.as_view(),
        name="update-permissions",
    ),
]
