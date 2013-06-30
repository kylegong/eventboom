import base64
from datetime import datetime

# Django
from django.core import exceptions
from django.core.urlresolvers import reverse
from django.db import models

# Third-party
from Crypto import Random
from stdimage import StdImageField

DEFAULT_CHAR_FIELD_LENGTH = 255
DEFAULT_TOKEN_LENGTH = 48

def generate_random_token(token_length=DEFAULT_TOKEN_LENGTH):
    byte_length = token_length * 6 / 8
    return base64.urlsafe_b64encode(Random.new().read(byte_length))


# Models
class Event(models.Model):
    IMAGE_PATH = "images/event"

    title = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    datetime = models.DateTimeField(default=datetime.now())
    # more sophisticated location?
    location = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH,
                                blank=True, null=True)
    # Neighborhood validation disabled
    neighborhood = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH) #choices=NEIGHBORHOODS)
    description = models.TextField(blank=True, null=True)
    min_attendees = models.IntegerField(blank=True, null=True)
    max_attendees = models.IntegerField(blank=True, null=True)
    image = StdImageField(upload_to=IMAGE_PATH, size=(1024, 1024),
                          blank=True, null=True)

    FULL_VALUES = (
        'id',
        'title',
        'location',
        'description',
        'neighborhood',
        'min_attendees',
        'max_attendees',
    )

    UPDATE_FIELDS = (
        'title',
        'datetime',
        'location',
        'neighborhood',
        'description',
        'min_attendees',
        'max_attendees',
        'image',
    )

    def as_dict(self):
        d = {field: getattr(self, field) for field in Event.FULL_VALUES}
        d['datetime'] = str(self.datetime)
        d['tags'] = [tag.tag_name for tag in self.tags.all()]
        if self.image:
            d['image'] = self.image.url
        return d

    def get_email_update_url(self):
        token = self.creator.token
        base_url = reverse('email_update', kwargs={'event_id': self.id})
        return '%s?t=%s' % (base_url, token)


class Tag(models.Model):
    BREAKING_BREAD = 'breaking bread'
    FELLOWSHIP = 'fellowship'
    GAMES = 'games'
    MUSIC = 'music'
    PRAYER = 'prayer'
    SPORTS = 'sports'
    OTHER = 'other'
    TAG_CHOICES = (
        (BREAKING_BREAD, BREAKING_BREAD),
        (FELLOWSHIP, FELLOWSHIP),
        (GAMES, GAMES),
        (MUSIC, MUSIC),
        (SPORTS, SPORTS),
        (OTHER, OTHER),
    )
    tag_name = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH,
                                choices=TAG_CHOICES)
    event = models.ForeignKey('Event', related_name='tags')


class UserProfile(models.Model):
    display_name = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    token = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH,
                             default=generate_random_token, blank=True, null=True)

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

    def clean_fields(self, *args, **kwargs):
        self.phone = UserProfile._validate_phone(self.phone)
        super(UserProfile, self).clean_fields(*args, **kwargs)

    FULL_VALUES = (
                'id',
                'display_name',
                'email',
                'phone',
    )

    def as_dict(self):
        return {field: getattr(self, field)
            for field in UserProfile.FULL_VALUES}

