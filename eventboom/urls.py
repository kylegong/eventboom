from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from events import views

urlpatterns = patterns('',
    url(r'^api/v1/events/(?P<event_id>\d+)/$', views.event, name='event'),
    url(r'^api/v1/events/$', views.events, name='events'),
    url(r'^api/v1/neighborhoods/$', views.get_neighborhoods,
        name='get_neighborhoods'),
    url(r'^api/v1/tags/$', views.get_tags, name='get_tags'),

    url(r'^email/events/(?P<event_id>\d+)/$', views.email_update,
        name='email_update'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
