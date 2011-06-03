
from django import template
from django.conf import settings
import datetime
from meetings.models import Meeting
from meetings.meeting_threadlocal import get_current_user


register = template.Library()

def acurrent_time():
    return datetime.datetime.now()
register.simple_tag(acurrent_time)

def get_meeting(start,end,empty_msg):
    return {
	'meetings':Meeting.objects.all().order_by('when')[start:end],
	'empty_msg':empty_msg,
        'user': get_current_user()
    }
register.inclusion_tag('meetings/meeting_block.html')(get_meeting)

def get_future_meeting(start,end,empty_msg):
    return {
	'meetings':Meeting.objects.filter(
            when__gte=datetime.datetime.now()-settings.LATE_ARRIVAL_OFFSET
            ).order_by('when')[start:end],
	'empty_msg':empty_msg,
        'user': get_current_user()
    }
register.inclusion_tag('meetings/meeting_block.html')(get_future_meeting)

def get_all_past_meetings(empty_msg):
    return {
	'meetings':Meeting.objects.filter(when__lte=datetime.datetime.now() ), 
	'empty_msg':empty_msg,
        'user': get_current_user()
    }
register.inclusion_tag('meetings/meeting_block.html')(get_all_past_meetings)
 

