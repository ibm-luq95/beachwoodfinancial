# -*- coding: utf-8 -*-#

from rest_framework import routers

from document.views import DocumentViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"document-api", DocumentViewSet, basename="document-api-router")

# urlpatterns = [path("update/<uuid:pk>", UpdateJobApiView.as_view(), name="update")]

# urlpatterns = []
urlpatterns = router.urls
# import pprint
# pprint.pprint(router.get_urls())
