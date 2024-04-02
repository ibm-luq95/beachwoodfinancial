# -*- coding: utf-8 -*-#

from rest_framework import routers

from job_category.views import JobCategoryViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(
    r"job-category-api", JobCategoryViewSet, basename="job-category-api-router"
)

urlpatterns = router.urls
