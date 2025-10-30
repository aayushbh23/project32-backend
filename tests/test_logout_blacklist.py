import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_logout_blacklists_refresh_token(django_user_model):
    user = django_user_model.objects.create_user(
        email="u@example.com", password="StrongPass123!", first_name="U", last_name="X"
    )
    client = APIClient()

    # Obtain tokens
    resp = client.post(reverse("login"), {"email": "u@example.com", "password": "StrongPass123!"})
    assert resp.status_code == 200
    access = resp.data["access"]
    refresh = resp.data["refresh"]

    # Auth with access, then logout using refresh
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
    logout_resp = client.post(reverse("logout"), {"refresh": refresh}, format="json")
    assert logout_resp.status_code == 204

    # Trying to rotate with a blacklisted refresh should now fail
    rotate = client.post(reverse("token_refresh"), {"refresh": refresh}, format="json")
    assert rotate.status_code in (401, 400)
    # Many configs return 401 with code "token_blacklisted"
