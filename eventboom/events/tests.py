import json
import urllib

from django.core import exceptions
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from eventboom.events import models

class TestUserProfile(TestCase):
    def test_token(self):
        user_profile1 = models.UserProfile(display_name="Test User 1")
        self.assertEquals(len(user_profile1.token), 48)
        user_profile2 = models.UserProfile(display_name="Test User 2")
        self.assertEquals(len(user_profile2.token), 48)
        self.assertNotEqual(user_profile1.token, user_profile2.token)

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

class TestViews(TestCase):
    def test_create_event(self):
        TEST_DATA = {
            'event': json.dumps({
                'id': 1,
                'title': 'My event',
                'description': "Stuff",
                'datetime': "2013-05-01",
                'tags': ['sports', 'breaking_bread'],
                'location': 'Lolinda',
                'neighborhood': 'soma',
                'creator_name': 'Charles Bartowski',
            }),
            'user_profile': json.dumps({
                'display_name': 'KG',
                'email': 'kylegong@gmail.com',
                'phone': '8888888888',
            }),
        }
        c = Client()
        url = reverse('events')
        response = c.post(url, data=TEST_DATA)
        self.assertEquals(response.status_code, 200)
        events = models.Event.objects.all()
        self.assertEquals(len(events), 1)
        user_profiles = models.UserProfile.objects.all()
        self.assertEquals(len(user_profiles), 1)
        self.assertEquals(len(events[0].tags.all()), 2)
