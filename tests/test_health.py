import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_health(client):
    url = reverse("health-check")
    resp = client.get(url)
    assert resp.status_code == 200
    data = resp.json()
    assert data.get("status") in {"ok", "healthy", "up"}
