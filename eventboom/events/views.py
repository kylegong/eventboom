import json

from django import http

from models import Event

def render_as_json(data_dict):
    return http.HttpResponse(json.dumps(data_dict),
                             content_type='application/json')

def get_events(request):
    data = {
        'events': list(Event.objects.all().values(
            'title',
            'location',
        ))
    }
    return render_as_json(data)
