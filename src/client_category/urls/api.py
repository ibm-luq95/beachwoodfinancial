# -*- coding: utf-8 -*-#

from rest_framework import routers

from client_category.views import ClientCategoryViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(
    r"client-category-api", ClientCategoryViewSet, basename="client-category-api-router"
)

urlpatterns = router.urls
