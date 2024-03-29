# -*- coding: utf-8 -*-#
from django.urls import path, include
from client_account.views import (
    ClientAccountDeleteView,
    ClientAccountCreateView,
    ClientAccountListViewBW,
    ClientAccountUpdateView,
)

app_name = "client_account"

urlpatterns = [
    path("", ClientAccountListViewBW.as_view(), name="list"),
    path("create", ClientAccountCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", ClientAccountUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", ClientAccountDeleteView.as_view(), name="delete"),
    path("api/", include("client_account.urls.api"), name="api"),
]
