import pytest
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_axes_login_lockout_after_five_failures(client: Client):
    login_url = reverse("auth:login")
    
    # Trigger 5 failed login attempts
    for _ in range(5):
        client.post(login_url, {"email": "nonexistent@example.com", "password": "wrongpassword", "user_type": "manager"})
    
    # 6th attempt must be blocked by Axes (HTTP 403)
    response6 = client.post(login_url, {"email": "nonexistent@example.com", "password": "wrongpassword", "user_type": "manager"})
    assert response6.status_code == 403

