# Django
from django.core import exceptions
from django.db import models

# Third-party
from django_extensions.db.fields import UUIDField
from stdimage import StdImageField

DEFAULT_CHAR_FIELD_LENGTH = 255

# Models
class Event(models.Model):
    IMAGE_PATH = "images/event"

    title = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    datetime = models.DateTimeField(blank=True, null=True)
    # more sophisticated location?
    location = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH,
                                blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    min_attendees = models.IntegerField(blank=True, null=True)
    max_attendees = models.IntegerField(blank=True, null=True)
    creator = models.ForeignKey('UserProfile')
    image = StdImageField(upload_to=IMAGE_PATH, size=(300, 300),
                                   blank=True, null=True)


class UserProfile(models.Model):
    IMAGE_PATH = "images/user_profile"
    DEFAULT_TOKEN_BITLENGTH = 64

    display_name = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    email = models.EmailField(blank=True, null=True)
    # Store digits only here
    phone = models.CharField(max_length=10, blank=True, null=True)
    image = StdImageField(upload_to=IMAGE_PATH, size=(300, 300),
                                   blank=True, null=True)
    uuid = UUIDField()

    @staticmethod
    def validate_phone(phone_number):
        phone_number = ''.join([c for c in phone_number if c in '1234567890'])
        if phone_number[0] == '1':
            phone_number = phone_number[1:]
        if phone_number < 10:
            raise exceptions.ValidationError
        else:
            return phone_number[:10]

    def clean_fields(self, *args, **kwargs):
        self.phone = UserProfile.validate_phone(self.phone)
        super(UserProfile, self).clean_fields(*args, **kwargs)

