from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')

email = 'test@londonappdev.com'


def create_user(**params):
    """Helper function to create new user"""
    return get_user_model().objects.create_user(**params)


def factoryPayload(email, password, name='un nombre'):
    return {
        'email': email,
        'password': password,
        'name': name,
    }


class PublicUserApiTests(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_ok_create_valid_user_success(self):
        payload = factoryPayload(email, 'testpass', 'dummy')
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(**res.data)
        self.assertTrue(
            user.check_password(payload['password'])
        )
        self.assertNotIn('password', res.data)

    def test_error_if_user_exists(self):
        payload = factoryPayload(email, 'testpass', 'dummy')
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_error_if_password_too_short(self):
        payload = factoryPayload(email, 'pw', 'dummy')
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        lista_all_user = get_user_model().objects
        is_exists_user = lista_all_user.filter(
            email=payload['email']
        ).exists()

        self.assertFalse(is_exists_user)
