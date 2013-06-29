from django.core import exceptions
from django.test import TestCase

from eventboom.events import models

class TestUserProfile(TestCase):
    def test_phone_validation(self):
        """
        Tests that phone numbers are properly saved to the db.
        """
        TEST_DATA = (
            # phone_input, expected
            # if expected = None, validation should fail
            ('1-234-567-8901', '2345678901'),
            ('234-567-8901', '2345678901'),
            ('(234) 567-8901', '2345678901'),
            ('234.567.8901', '2345678901'),
            ('2345678901234567890', '2345678901'),
            ('', ''),
            ('555-5555', None),
        )
        for phone_input, expected in TEST_DATA:
            user_profile = models.UserProfile(display_name="Test User 1",
                phone=phone_input)
            if expected is None:
                self.assertRaises(exceptions.ValidationError,
                                  user_profile.full_clean())
            else:
                user_profile.full_clean()
                self.assertEquals(user_profile.phone, expected)
