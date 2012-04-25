from django.db import models
from django.contrib.auth.models import User
from meetings.meeting_threadlocal import get_current_user
import settings
import datetime
# Create your models here.

MAX_LENGTH = 128

class Venue(models.Model):

    def __unicode__(self):
	return self.name

    name = models.CharField(max_length=MAX_LENGTH)
    email = models.EmailField(max_length=MAX_LENGTH,blank=True,null=True)
    phone = models.CharField(max_length=MAX_LENGTH,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)

    @property
    def jsonLatLng(self):
        '''
        Use the string returned as args for google.maps.LatLng constructor.
	'''
        if self.latitude != None and self.longitude != None:
            return "%.6f,%.6f" % (self.latitude,self.longitude)
        else:
            return None
    
    directions = models.TextField(blank=True,null=True)
    embed_map = models.TextField(blank=True,null=True)
    link = models.URLField(verify_exists=True, blank=True, null=True)

MEETING = (
    ('Loop', 'Loop Meeting - 2nd Thursday'),
    ('North', 'North Meeting - 3rd Thursday')
)

class Meeting(models.Model):


    def __unicode__(self):
	if self.venue:
	    return "%s at %s" % (self.when.strftime("%A, %B %d %Y at %I:%M %p"), self.venue.name)
	return "%s location TBD" % self.when

    when = models.DateTimeField()
    venue = models.ForeignKey(Venue,blank=True,null=True)
    which = models.CharField(max_length=5,choices=MEETING)

    stamp_created = models.DateTimeField(auto_now_add=True)
    stamp_modified = models.DateTimeField(auto_now=True)
    
    def is_future(self):
        return bool( self.when >=  ( datetime.datetime.now()-settings.LATE_ARRIVAL_OFFSET ) )

    def rsvp_user_yes(self):
    	return self.meetingrsvp_set.filter(user=get_current_user(),rsvp='yes').count() != 0

    def rsvp_user_maybe(self):
    	return self.meetingrsvp_set.filter(user=get_current_user(),rsvp='maybe').count() != 0


class Presentor(models.Model):
    def __unicode__(self):
	return self.name

    name = models.CharField(max_length=MAX_LENGTH)
    email = models.EmailField(max_length=MAX_LENGTH,blank=True,null=True)
    phone = models.CharField(max_length=MAX_LENGTH,blank=True,null=True)

LENGTH_CODES =(
    ('5',':05 Five Minutes'),
    ('10',':10 Ten Minutes'),
    ('15',':15 Fifteen Minutes'),
    ('20',':20 Twenty Minutes'),
    ('25',':25 Twenty-Five Minutes'),
    ('30',':30 Thirty Minutes'),
    ('45',':45 Forty-Five Minutes'),
    ('50',':50 Fifty Minutes'),
    ('60','1:00 One Hour'),
    ('TBD','To be determined'),
)

 
class Topic(models.Model):

    def __unicode__(self):
	out = self.title
	#if self.by:
	#    out += "By: %s" % self.by.name
	return out

    title = models.CharField(max_length=MAX_LENGTH)
    #by = models.ForeignKey(Presentor,blank=True,null=True)
    presentors = models.ManyToManyField(Presentor)
    meeting = models.ForeignKey( Meeting, blank=True, null=True)
    length = models.CharField(max_length=4,choices=LENGTH_CODES)
    embed_video = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    slides_link = models.URLField(verify_exists=True, blank=True, null=True)
    start_time = models.DateTimeField(blank = True, null = True)

    stamp_created = models.DateTimeField(auto_now_add=True)
    stamp_modified = models.DateTimeField(auto_now=True)
    
    def presentor_names(self):
      print self.presentors.all()
      return ", ".join(map(lambda p: p.name, self.presentors.all())) #I imagine this would cause a n+1, not sure how to prefetch many-to-many

class TopicLink(models.Model):
    
    def __unicode__(self):
	return "%s -> %s" % (self.topic.title, self.link_title)

    link_title = models.CharField(max_length=MAX_LENGTH)
    link = models.URLField(verify_exists=True)
    topic = models.ForeignKey(Topic)

    stamp_created = models.DateTimeField(auto_now_add=True)
    stamp_modified = models.DateTimeField(auto_now=True)

class MeetingRsvp(models.Model):
    
    def __unicode__(self):
        return "%s for %s" % (self.user, self.meeting)

    meeting = models.ForeignKey(Meeting)
    user = models.ForeignKey( User )
    rsvp = models.CharField(max_length=5,choices=( 
		('yes','yes'), 
		('maybe','maybe') 
	)
    )

    stamp_created = models.DateTimeField(auto_now_add=True)
    stamp_modified = models.DateTimeField(auto_now=True)


