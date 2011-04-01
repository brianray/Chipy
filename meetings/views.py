from models import Topic
from django.shortcuts import render_to_response, get_object_or_404

def embed_video(request,id):
    topic = get_object_or_404(Topic, pk=id)
    return render_to_response(
        'meetings/embed.html',
        {'topic':topic})

	
