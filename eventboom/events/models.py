import base64

# Django
from django.core import exceptions
from django.core.urlresolvers import reverse
from django.db import models

# Third-party
from Crypto import Random
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

    FULL_VALUES = (
        'id',
        'title',
        'datetime',
        'location',
        'description',
        'min_attendees',
        'max_attendees',
        'creator_id',
        'creator__image',
    )

    LIST_VALUES = (
        'id',
        'title',
        'datetime',
        'location',
    )

    UPDATE_FIELDS = (
        'title',
        'datetime',
        'location',
        'description',
        'min_attendees',
        'max_attendees',
        'image',
    )

    def as_dict(self):
        return {field: getattr(self, field) for field in Event.FULL_VALUES}

    def get_email_update_url(self):
        token = self.creator.token
        base_url = reverse('email_update', kwargs={'event_id': self.id})
        return '%s?t=%s' % (base_url, token)

class UserProfile(models.Model):
    IMAGE_PATH = "images/user_profile"
    DEFAULT_TOKEN_BITLENGTH = 64

    display_name = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    email = models.EmailField(blank=True, null=True)
    # Store digits only here
    phone = models.CharField(max_length=10, blank=True, null=True)
    image = StdImageField(upload_to=IMAGE_PATH, size=(300, 300),
                          blank=True, null=True)
    token = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH, null=True, blank=True)

    @staticmethod
    def generate_random_token(bitlength=DEFAULT_TOKEN_BITLENGTH):
        return base64.urlsafe_b64encode(Random.new().read(bitlength))

    @staticmethod
    def _validate_phone(phone_number):
        if not phone_number:
            return ''
        phone_number = ''.join([c for c in phone_number if c in '1234567890'])
        if phone_number[0] == '1':
            phone_number = phone_number[1:]
        if phone_number < 10:
            raise exceptions.ValidationError
        else:
            return phone_number[:10]

    def save(self, *args, **kwargs):
        # Only generate token on first write
        if not self.pk:
            self.token = UserProfile.generate_random_token()
        super(UserProfile, self).save(*args, **kwargs)

    def clean_fields(self, *args, **kwargs):
        self.phone = UserProfile._validate_phone(self.phone)
        super(UserProfile, self).clean_fields(*args, **kwargs)

    FULL_VALUES = (
                'id',
                'display_name',
                'email',
                'phone',
                'image',
    )

    def as_dict(self):
        return {field: getattr(self, field)
            for field in UserProfile.FULL_VALUES}

