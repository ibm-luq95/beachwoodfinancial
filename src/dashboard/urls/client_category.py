# -*- coding: utf-8 -*-#
from django.urls import path
from client_category.views import ClientCategoryListView, ClientCategoryCreateView

app_name = "client_category"

urlpatterns = [
    path("", ClientCategoryListView.as_view(), name="list"),
    path("create", ClientCategoryCreateView.as_view(), name="create"),
]
