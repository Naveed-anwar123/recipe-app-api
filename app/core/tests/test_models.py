from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test user creation with email"""
        email = 'test@london.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
        email=email,
        password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test that email address is normalized"""
        email = 'test@LONDON.COM'
        user = get_user_model().objects.create_user(email,'test124')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email"""
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(None,'test124')

    def test_create_new_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser('test@london.com','test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
