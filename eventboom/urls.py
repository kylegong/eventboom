from django.conf.urls import patterns, include, url

from events.views import GetEvents
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ihasinterests.views.home', name='home'),
    # url(r'^ihasinterests/', include('ihasinterests.foo.urls')),

    url(r'^api/v1/events/', GetEvents.as_view(), name='get_events'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
