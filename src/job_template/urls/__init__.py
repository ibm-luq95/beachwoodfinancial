# -*- coding: utf-8 -*-#
from django.urls import path, include
from job_template.views import JobTemplateListView

app_name = "job_template"

urlpatterns = [
    path("", JobTemplateListView.as_view(), name="list"),
    # path("create", "", name="create"),
    # path("update/<uuid:pk>", "", name="update"),
    # path("delete/<uuid:pk>", "", name="delete"),
]
