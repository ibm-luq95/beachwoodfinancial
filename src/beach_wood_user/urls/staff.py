# -*- coding: utf-8 -*-#
from django.urls import path

from beach_wood_user.views import (
    StaffMemberDetailsView,
    UpdateStaffPermissionsApiView,
    AssignClientToBookkeeperApiView,
)

app_name = "staff"

urlpatterns = [
    path("<uuid:pk>/", StaffMemberDetailsView.as_view(), name="member-details"),
    path(
        "api/update-permissions/",
        UpdateStaffPermissionsApiView.as_view(),
        name="update-permissions",
    ),
    path(
        "api/assign-client/",
        AssignClientToBookkeeperApiView.as_view(),
        name="assign-client",
    ),
]
