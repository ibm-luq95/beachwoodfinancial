# -*- coding: utf-8 -*-#
from django.urls import path

from archive.views.special_assignment import SpecialAssignmentArchiveListView

app_name = "special_assignment"

urlpatterns = [
    path("archive", SpecialAssignmentArchiveListView.as_view(), name="list"),
]
