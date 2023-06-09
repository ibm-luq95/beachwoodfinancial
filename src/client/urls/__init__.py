# -*- coding: utf-8 -*-#
from django.urls import path, include

from client.views import ClientListView, ClientCreateView

app_name = "client"

urlpatterns = [
    path("", ClientListView.as_view(), name="list"),
    path("create", ClientCreateView.as_view(), name="create"),
]
