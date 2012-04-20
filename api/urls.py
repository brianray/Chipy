from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import MeetingHandler, PresentorHandler

meeting_handler = Resource(MeetingHandler)
presentor_handler = Resource(PresentorHandler)

urlpatterns = patterns('', 
    url(r'^meetings\.(?P<emitter_format>.+)', meeting_handler),
    url(r'^presentors\.(?P<emitter_format>.+)', presentor_handler),
    )


