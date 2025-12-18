from django.shortcuts import render
from .models import StoryEvent

def story_view(request):
    story_events = StoryEvent.objects.filter(is_active=True).order_by('order')
    featured_events = story_events.filter(is_featured=True)
    
    context = {
        'story_events': story_events,
        'featured_events': featured_events
    }
    return render(request, 'story.html', context)
