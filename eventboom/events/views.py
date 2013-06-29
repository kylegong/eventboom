import json

from django.http import HttpResponse, Http404

from models import Event, UserProfile

def render_as_json(data_dict):
    return HttpResponse(json.dumps(data_dict),
                             content_type='application/json')

def events(request):
    # READ: Gets all events in database
    if request.method == "GET":
        return get_events(request)

    # CREATE: Add a new event
    elif request.method == "POST":
        return post_events(request)

    # UPDATE: change an existing event
    elif request.method == "UPDATE":
        return update_events(request)

    raise Http404

def get_events(request):
    data = list(Event.objects.all().values(
            'id',
            'title',
            'location',
    ))
    return render_as_json(data)

def get_event(request, event_id):
    data = list(Event.objects.filter(id=event_id).values(
            'id',
            'title',
            'location',
    ))[0]
    return render_as_json(data)

def post_events(request):
    new_event = request.POST
    user_profile = UserProfile.objects.create(
            display_name = new_event["display_name"],
            email = new_event.get("email"),
            phone = new_event.get("phone"),
    )

    event = Event.objects.create(
        title=new_event["title"],
        creator=user_profile,
    )

    return get_event(request, event.id)

def update_events(request):
    data = {
    }
    return render_as_json(data)
