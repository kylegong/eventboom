import json

from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseForbidden
from django.http import HttpResponseNotFound

from models import Event, UserProfile

def render_as_json(data_dict):
    return HttpResponse(json.dumps(data_dict), content_type='application/json')

def events(request):
    if request.method == "GET":
        return get_events(request, event_id)

    elif request.method == "POST":
        return create_event(request, event_id)

def get_events(request):
    data = list(Event.objects.all().values(Event.LIST_VALUES))
    return render_as_json(data)

def create_event(request):
    event_data = json.loads(request.POST.get('event'))
    user_profile_data = json.loads(request.POST.get('user_profile'))
    user_profile = UserProfile.objects.create(user_profile_data)
    event = Event.objects.create(event_data)

    if errors:
        return render_as_json({'errors': errors})

    data = {
        'event': event,
        'user_profile': user_profile,
    }
    return render_as_json(data)

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
        user_profile_data = json.loads(request.POST.get('user_profile'))
    except ValueError:
        return HttpResponseBadRequest()
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return HttpResponseNotFound()
    creator = event.creator
    if not 'token' in user_profile_data:
        return HttpResponseBadRequest()
    if not user_profile_data['token'] == event.creator.uuid:
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
