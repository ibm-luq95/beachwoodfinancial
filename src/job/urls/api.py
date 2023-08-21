# -*- coding: utf-8 -*-#
from django.urls import path, include

from job.views import UpdateJobApiView, JobViewSet
from rest_framework import routers

app_name = "api"

router = routers.DefaultRouter()
router.register(r"jobs-api", JobViewSet, basename="job-api-router")

# urlpatterns = [path("update/<uuid:pk>", UpdateJobApiView.as_view(), name="update")]

# urlpatterns = []
urlpatterns = router.urls
# import pprint
# pprint.pprint(router.get_urls())
