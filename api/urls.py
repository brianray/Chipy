from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import MeetingHandler, PresentorHandler

meeting_handler = Resource(MeetingHandler)
presentor_handler = Resource(PresentorHandler)

urlpatterns = patterns('', 
    url(r'^meeting/(?P<meeting_id>[^/]+)/', meeting_handler),
    url(r'^meetings/', meeting_handler),
    url(r'^presentor/(?P<presentor_id>[^/]+)/', presentor_handler),
    url(r'^presentors/', presentor_handler),
    )


