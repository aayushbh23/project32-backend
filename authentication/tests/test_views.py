import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from users.tests.factories import UserFactory


@pytest.mark.django_db
def test_register_and_login():
    client = APIClient()
    # Test registration
    resp = client.post(reverse('register'), {
        'email': 'new@example.com',
        'password': 'StrongPass123!',
        'first_name': 'firstName',
        'last_name': 'last_name'
    })
    assert resp.status_code == 201

    # Test login
    resp = client.post(reverse('login'), {
                       'email': 'new@example.com', 'password': 'StrongPass123!'})
    assert resp.status_code == 200
    assert 'access' in resp.data and 'refresh' in resp.data
