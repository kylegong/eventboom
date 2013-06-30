import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseForbidden
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.conf import settings

from forms import EventForm, UserProfileForm
from models import Event, UserProfile

USER_TOKEN = 'user_token'

def render_as_json(data_dict, cookie_dict=None):
    response = HttpResponse(json.dumps(data_dict),
                            content_type='application/json')
    if cookie_dict:
        for k, v in cookie_dict.items():
            response.set_cookie(k, v)
    return response



def events(request):
    if request.method == "GET":
        return get_events(request)

    elif request.method == "POST":
        return create_event(request)



def get_events(request):
    data = [e.as_dict() for e in Event.objects.all()]
    return render_as_json(data)



def create_event(request):
    event_data = json.loads(request.POST.get('event'))
    user_profile_data = json.loads(request.POST.get('user_profile'))

    user_profile = None
    if USER_TOKEN in request.COOKIES:
        try:
            user_profile = UserProfile.objects.get(
                token=request.COOKIES[USER_TOKEN])
        except UserProfile.DoesNotExist:
            pass
    if not user_profile:
        user_profile = UserProfileForm(user_profile_data, request.FILES).save()

    # Create event
    event_data['tag'] = event_data['tags'][0]
    form = EventForm(event_data)
    import sys
    sys.stderr.write(str(form.errors))
    event = form.save()

    data = {
        'event': event.as_dict(),
        'user_profile': user_profile.as_dict(),
    }
    cookie_dict = {
        USER_TOKEN: user_profile.token
    }
    return render_as_json(data, cookie_dict)

def event(request, event_id):
    if request.method == "GET":
        return get_event(request, event_id)

    elif request.method == "POST":
        return update_event(request, event_id)

def get_event(request, event_id):
    event = list(Event.objects.filter(id=event_id).values(Event.FULL_VALUES))
    data = {
        'event': event,
    }
    return render_as_json(data)

def update_event(request, event_id):
    try:
        event_data = json.loads(request.POST.get('event'))
    except ValueError:
        return HttpResponseBadRequest()
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return HttpResponseNotFound()
    creator = event.creator
    if not USER_TOKEN in request.COOKIES:
        return HttpResponseBadRequest()
    if not request.COOKIES[USER_TOKEN] == event.creator.token:
        return HttpResponseForbidden()
    for field, value in event_data:
        if field in Event.UPDATE_FIELDS:
            setattr(event, field, value)
    try:
        event.save()
    except:
        return HttpResponseBadRequest()
    data = {
        'event': event.as_dict(),
    }
    return render_as_json(data)

def email_update(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return HttpResponseNotFound()
    response = HttpResponseRedirect(reverse('event',
                                    kwargs={'event_id': event_id}))
    if 't' in self.request.GET:
        if self.request.GET['t'] == event.creator.token:
            response.set_cookie(USER_TOKEN, event.creator.token)
    return response
