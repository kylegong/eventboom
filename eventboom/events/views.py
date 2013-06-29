import json

from django.http import HttpResponse, Http404

from models import Event

def render_as_json(data_dict):
    return HttpResponse(json.dumps(data_dict),
                             content_type='application/json')

def events(request):
    if request.method == "GET":
        return get_events(request)
    elif request.method == "POST":
        return post_events(request)
    elif request.method == "UPDATE":
        return update_events(request)

    raise Http404

def get_events(request):
    data = {
        'events': list(Event.objects.all().values(
            'title',
            'location',
        ))
    }
    return render_as_json(data)

def post_events(request):
    data = {

    }
    return render_as_json(data)

def update_events(request):
    data = {
    }
    return render_as_json(data)
