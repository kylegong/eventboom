# Copied from https://docs.djangoproject.com/en/1.4/topics/class-based-views/#more-than-just-html
from django import http
from django.utils import simplejson as json
from django.views.generic import ListView

from events.models import Event

# Django's class-based views return http/html responses by default
# This simple mix-in, copied from url at top, overrides this behavior
# to return JSON instead
class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

# This Class-based list view just sets which model to use for the subsequent REST calls we will write
class EventsBase(ListView):
    context_object_name = "events_list"
    
    def get_queryset(self):
        return Events.objects.all()


# CRUD call GET to Events (Read)
# This is a Read call to the Events collection: "GET api/v1/events" should call this and return list of all events
class GetEvents(JSONResponseMixin, EventsBase):
    def convert_context_to_json(self, context):
        context['events_list'] = Events.objects.values('title', 'location')
        return json.dumps(context)
