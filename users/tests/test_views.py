import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from .factories import UserFactory


@pytest.mark.django_db
def test_profile_and_update():
    client = APIClient()
    user = UserFactory()
    client.force_authenticate(user=user)

    # Test profile retrieve
    resp = client.get(reverse('profile'))
    assert resp.status_code == 200
    assert resp.data['email'] == user.email

    # Test profile update
    resp = client.patch(reverse('profile-update'), {'display_name': 'NewName'})
    assert resp.status_code == 200
    assert resp.data['display_name'] == 'NewName'
