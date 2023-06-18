from django.urls import path

from job_category.views import (
    JobCategoryCreateView,
    JobCategoryListView,
    JobCategoryDeleteView,
    JobCategoryUpdateView,
)

app_name = "job_category"

urlpatterns = [
    path("", JobCategoryListView.as_view(), name="list"),
    path("create", JobCategoryCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", JobCategoryUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", JobCategoryDeleteView.as_view(), name="delete"),
]
