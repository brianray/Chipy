from piston.handler import BaseHandler
from meetings.models import Meeting

class MeetingHandler(BaseHandler):
  allowed_methods = ('GET',)
  model = Meeting

  def read(self, request, meeting_id=None):
    print request
    base = Meeting.objects
    if meeting_id:
      return base.get(pk=meeting_id)
    else:
      return base.all()
