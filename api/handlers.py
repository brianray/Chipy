from piston.handler import BaseHandler
from meetings.models import Meeting, Presentor

class MeetingHandler(BaseHandler):
  allowed_methods = ('GET',)
  model = Meeting
  fields = ('when', 'which', ('venue', ('name',)), ('topic_set', ('title', 'description', 'length', 'start_time', ('presentor_set', ('name',)))))

  def read(self, request, meeting_id=None):
    base = Meeting.objects
    if meeting_id:
      print(meeting_id)
      return base.get(pk=meeting_id) 
    else:
      return base.all()

class PresentorHandler(BaseHandler):
  allowed_methods = ('GET',)
  model = Presentor
  fields = ('name', 'email', 'phone', ('topic_set', ('title','description', 'length', 'start_time')))

  def read(self, request, presentor_id=None):
      base = Presentor.objects
      if presentor_id:
        return base.get(pk=presentor_id)
      return base.all()
