from models import Topic
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from meetings.models import Rsvp, Meeting
from datetime import *

def embed_video(request,id):
    topic = get_object_or_404(Topic, pk=id)
    return render_to_response(
        'meetings/embed.html',
        {'topic':topic})

#Not finished	
def rsvp_update(request):
    if request.user.is_authenticated():
        rsvpname = request.user.username
        rsvp_answer = request.POST.get('answer')
        q1 = Meeting.objects.filter(when__gte=datetime.now())[0].pk
        m = Meeting.objects.get(pk=q1)
        r = m.rsvp_set.create(name=rsvpname, rsvp=rsvp_answer) 
        r.save()
        message = "Thanks for RSVP'ing!"
    else:
        message = 'You need to be logged in to do that.'
    return HttpResponse(message)
