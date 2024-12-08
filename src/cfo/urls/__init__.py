# -*- coding: utf-8 -*-#
from django.urls import path, include

from cfo.views.cfo import CFOListView, CFOCreateView

app_name = "management_cfo"

urlpatterns = [
    path("", CFOListView.as_view(), name="list"),
    path("create", CFOCreateView.as_view(), name="create"),
    # path("update/<uuid:pk>", BookkeeperUpdateView.as_view(), name="update"),
    # path("delete/<uuid:pk>", BookkeeperDeleteView.as_view(), name="delete"),
    # path("<uuid:pk>", BookkeeperDetailsView.as_view(), name="details"),
]
