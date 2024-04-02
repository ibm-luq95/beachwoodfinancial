# -*- coding: utf-8 -*-#
from django.urls import path, include
from client_category.views import (
    ClientCategoryListViewBW,
    ClientCategoryCreateView,
    ClientCategoryUpdateView,
    ClientCategoryDeleteView,
)

app_name = "client_category"

urlpatterns = [
    path("", ClientCategoryListViewBW.as_view(), name="list"),
    path("create", ClientCategoryCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", ClientCategoryUpdateView.as_view(), name="update"),
    path("api/", include("client_category.urls.api"), name="api"),
    path("delete/<uuid:pk>", ClientCategoryDeleteView.as_view(), name="delete"),
]
