# -*- coding: utf-8 -*-#
from django.urls import path

from beach_wood_user.views import StaffMemberDetailsView

app_name = "staff"

urlpatterns = [
    path("<uuid:pk>/", StaffMemberDetailsView.as_view(), name="member-details")
]
