from models import Topic
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from meetings.models import MeetingRsvp, Meeting
from datetime import *
from django.contrib import messages
import simplejson

def embed_video(request,id):
    topic = get_object_or_404(Topic, pk=id)
    return render_to_response(
        'meetings/embed.html',
        {'topic':topic})

def rsvp(request,mid,msg):
    if not request.user.is_authenticated():
	messages.error(request, 'You must login before you can RSVP.')
    	return redirect('/account/login/?next=%s'% request.path)
    
    message, ok = do_rsvp(
		msg,
		mid,
		request.user)
    if ok:
    	messages.success(request, message)
    else:
    	messages.error(request, message)

    return redirect('/')


def do_rsvp(msg,mid,user):
    ok = False

    if msg not in ('yes', 'maybe'):
        ok = False
        message = "Unknown reply %s" % msg
    elif user.is_authenticated():
        ok = True
        meeting  = Meeting.objects.get(pk=int(mid) )
        data = dict( user=user, meeting=meeting )
        r,created = MeetingRsvp.objects.get_or_create(**data)
        if not created:
	   if msg != r.rsvp:
               message = "Updated your RSVP status from %s to %s" % ( r.rsvp, msg)
               r.rsvp = msg
           else:
               message = "You are already RSVP'd to this meeting"
               ok = False  
	else:
            message = "Thanks for RSVP'ing for: '%s'!" % meeting
            r.rsvp = msg
        r.save()
    else:
         message = "You must be logged in to RSVP"
         ok = False

    return message, ok

def rsvp_update(request):
    message, ok = do_rsvp(
		request.POST.get('answer'),
		request.POST.get('id'),
		request.user)
    if ok:
    	messages.success(request, message)
    else:
    	messages.error(request, message)

    return HttpResponse(str(ok))

def topics_json(request, meeting):
    meeting = get_object_or_404(Meeting, pk=meeting)
    topics = []
    for topic in meeting.topic_set.all():
        topics.append({'title' : topic.title,
        'presenter' : topic.by.name,
        'contact_email' : topic.by.email,
        'start_time' : meeting.when.isoformat(),
        'duration' : topic.length,
        'description': topic.description,
        'released' : True,
        })

    return HttpResponse(simplejson.dumps(topics), mimetype="application/json")

