# Django
from django.db import models
from django_extensions.db.fields import UUIDField

# Third-party
import stdimage

DEFAULT_CHAR_FIELD_LENGTH = 255

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
    image = stdimage.StdImageField(upload_to=IMAGE_PATH, size=(300, 300))


class UserProfile(models.Model):
    IMAGE_PATH = "images/user_profile"
    DEFAULT_TOKEN_BITLENGTH = 64

    display_name = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    email = models.EmailField(blank=True, null=True)
    # Store digits only here
    phone = models.CharField(max_length=10, blank=True, null=True)
    image = stdimage.StdImageField(upload_to=IMAGE_PATH, size=(300, 300))

    uuid = UUIDField()
