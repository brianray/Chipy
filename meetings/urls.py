from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^past/$','django.views.generic.simple.direct_to_template', {'template': 'meetings/past_index.html'}, 'past_meetings'),
    (r'^next/$','django.views.generic.simple.direct_to_template', {'template': 'meetings/next_index.html'}, 'next_meeting'),
    url(r'^embed_video/(?P<id>\d+)/$', embed_video, {},'embed_video'),
    (r'^rsvp_update$', 'Chipy.meetings.views.rsvp_update'),
)
