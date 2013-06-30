from django.forms import ModelForm

from models import Event, UserProfile, Tag

def process_event_data(event_data):
    tag_names = event_data.pop('tags')
    form = EventForm(event_data)
    event = form.save()
    for tag_name in tag_names:
        tag = event.tags.create(tag_name=tag_name)
    return event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = Event.UPDATE_FIELDS


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
