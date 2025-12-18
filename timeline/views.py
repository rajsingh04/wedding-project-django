from django.shortcuts import render
from .models import TimelineEvent

def timeline_view(request):
    timeline_events = TimelineEvent.objects.filter(is_active=True).order_by('order')
    
    context = {
        'timeline_events': timeline_events
    }
    return render(request, 'timeline.html', context)
