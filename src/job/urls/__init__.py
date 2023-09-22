from django.urls import path, include
from job.views import (
    JobDetailsView,
    JobCreateView,
    JobListView,
    JobDeleteView,
    JobUpdateView,
)

app_name = "job"

urlpatterns = [
    path("", JobListView.as_view(), name="list"),
    path("create", JobCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", JobUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", JobDeleteView.as_view(), name="delete"),
    path("<uuid:pk>", JobDetailsView.as_view(), name="details"),
    path("api/", include("job.urls.api"), name="api"),
]
