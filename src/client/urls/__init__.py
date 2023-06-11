# -*- coding: utf-8 -*-#
from django.urls import path, include

from client.views import ClientListViewBW, ClientCreateView

app_name = "client"

urlpatterns = [
    path("", ClientListViewBW.as_view(), name="list"),
    path("create", ClientCreateView.as_view(), name="create"),
]
