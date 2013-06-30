from django.forms import ModelForm

from models import Event, UserProfile

class EventForm(ModelForm):
    class Meta:
        model = Event

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
