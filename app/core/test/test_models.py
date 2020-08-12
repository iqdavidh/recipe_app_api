from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """Crear"""
        email = "dummy@productividadti.com.mx"
        password = "un pass"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_normalize(self):
        """Los correos se gaurdan con el dominio normalizado - pero el usaurio no se toca"""
        email = "dummy@Test.com"

        user = get_user_model().objects.create_user(
            email=email,
            password='no se ocupa en el test'
        )

        self.assertEqual(user.email, email.lower())

        email2 = "Dummy@test.com"
        user2 = get_user_model().objects.create_user(
            email=email2,
            password='no se ocupa en el test'
        )

        self.assertEqual(user2.email, email2)
