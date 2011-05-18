from django.db import models

# Create your models here.

MAX_LENGTH = 128

class Venue(models.Model):

    def __unicode__(self):
	return self.name

    name = models.CharField(max_length=MAX_LENGTH)
    email = models.EmailField(max_length=MAX_LENGTH,blank=True,null=True)
    phone = models.CharField(max_length=MAX_LENGTH,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
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
	    return "%s at %s" % (self.when, self.venue.name)
	return "%s location TBD" % self.when

    when = models.DateTimeField()
    venue = models.ForeignKey(Venue,blank=True,null=True)
    which = models.CharField(max_length=5,choices=MEETING)

    stamp_created = models.DateTimeField(auto_now_add=True)
    stamp_modified = models.DateTimeField(auto_now=True)

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
    ('TBD',':?? To be determined'),
)

 
class Topic(models.Model):

    def __unicode__(self):
	out = self.title
	if self.by:
	    out += "By: %s" % self.by.name
	return out

    title = models.CharField(max_length=MAX_LENGTH)
    by = models.ForeignKey(Presentor,blank=True,null=True)
    meeting = models.ForeignKey( Meeting, blank=True, null=True)
    length = models.CharField(max_length=4,choices=LENGTH_CODES)
    embed_video = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    slides_link = models.URLField(verify_exists=True, blank=True, null=True)

    stamp_created = models.DateTimeField(auto_now_add=True)
    stamp_modified = models.DateTimeField(auto_now=True)


class TopicLink(models.Model):
    
    def __unicode__(self):
	return "%s -> %s" % (self.topic.title, self.link_title)

    link_title = models.CharField(max_length=MAX_LENGTH)
    link = models.URLField(verify_exists=True)
    topic = models.ForeignKey(Topic)

    stamp_created = models.DateTimeField(auto_now_add=True)
    stamp_modified = models.DateTimeField(auto_now=True)

class Rsvp(models.Model):
    
    def __unicode__(self):
        return self.name

    meeting = models.ForeignKey(Meeting)
    name = models.CharField(max_length=30,unique=True)
    rsvp = models.CharField(max_length=5)


