from models import *
from django.contrib import admin

admin.site.register(Venue)
#admin.site.register(Meeting)
admin.site.register(Presentor)
admin.site.register(Topic)
admin.site.register(TopicLink)




class TopicInline(admin.StackedInline):
    model = Topic
    extra = 3
    exclude = [
    ]
   

 
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('when','venue','which','stamp_created','stamp_modified')
    list_filter =  ('which',)
    exclude = [
    ]
    #search_fields = ('email','vehicle__vin','first_name', 'last_name')
    inlines = [
        TopicInline,
    ]
admin.site.register(Meeting,MeetingAdmin)



