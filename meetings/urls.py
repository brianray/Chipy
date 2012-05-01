from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^past/$','django.views.generic.simple.direct_to_template', {'template': 'meetings/past_index.html'}, 'past_meetings'),
    (r'^next/$','django.views.generic.simple.direct_to_template', {'template': 'meetings/next_index.html'}, 'next_meeting'),
    url(r'^embed_video/(?P<id>\d+)/$', embed_video, {},'embed_video'),
    (r'^rsvp_update$', 'meetings.views.rsvp_update'),
    (r'^rsvp/(?P<mid>\d+)/(?P<msg>.+)$', 'meetings.views.rsvp'),
    url(r'(?P<meeting>\d+)/topics.json', topics_json, name="topics.json"),
    (r'^download_calendar$', 'meetings.views.download_calendar'),
)
