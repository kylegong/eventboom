# Django
from django.db import models

# Third-party
import stdimage
from Crypto.Random import random

DEFAULT_CHAR_FIELD_LENGTH

class Event(models.Model):
    title = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    datetime = models.DateTimeField(blank=True, null=True)
    # more sophisticated location?
    location = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH,
                                blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    min_attendees = models.IntegerField(blank=True, null=True)
    max_attendees = models.IntegerField(blank=True, null=True)
    creator = models.ForeignKey('User')


class User(models.Model):
    USER_IMAGE_PATH = "images/user"

    display_name = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    image = stdimage.StdImageField(upload_to=USER_IMAGE_PATH,
                                   size=(300, 300))
    account = models.ForeignKey('Account')


class Account(models.Model):
    DEFAULT_TOKEN_BITLENGTH = 64

    token = models.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH,
                             blank=True)

    @staticmethod
    def generate_random_token(bitlength=DEFAULT_TOKEN_BITLENGTH):
        return base64.urlsafe_b64encode(Random.new().read(bitlength))
