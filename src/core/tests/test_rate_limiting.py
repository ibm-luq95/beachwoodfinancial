import pytest
from rest_framework.test import APIClient
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import path
from core.api.throttling import AuthEndpointRateThrottle

class DummyAuthAPIView(APIView):
    permission_classes = []
    throttle_classes = [AuthEndpointRateThrottle]
    
    def post(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)

@pytest.mark.django_db
def test_auth_endpoint_rate_limiting(rf):
    view = DummyAuthAPIView.as_view()
    
    # 5 requests should pass
    for _ in range(5):
        request = rf.post("/dummy-auth/")
        response = view(request)
        assert response.status_code == 200

    # 6th request within 1 minute must return HTTP 429
    request = rf.post("/dummy-auth/")
    response = view(request)
    assert response.status_code == 429

