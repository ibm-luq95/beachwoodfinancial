from django.urls import include, path

from job.views import (
    JobCreateView,
    JobDeleteView,
    JobDetailsView,
    JobListView,
    JobUpdateView,
    JobWorkstationView,
)


app_name = "job"

urlpatterns = [
    path("", JobListView.as_view(), name="list"),
    path("workstation/", JobWorkstationView.as_view(), name="workstation"),
    path("create", JobCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", JobUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", JobDeleteView.as_view(), name="delete"),
    path("<uuid:pk>", JobDetailsView.as_view(), name="details"),
    path("api/", include("job.urls.api"), name="api"),
]
