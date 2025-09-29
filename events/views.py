from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event


def event_list(request):
    """List all events with filtering"""
    events = Event.objects.filter(is_active=True)
    
    # Filtering
    event_type = request.GET.get('event_type')
    city = request.GET.get('city')
    date_filter = request.GET.get('date_filter')
    
    if event_type:
        events = events.filter(event_type=event_type)
    if city:
        events = events.filter(city__icontains=city)
    if date_filter == 'upcoming':
        events = events.filter(date__gte=timezone.now())
    elif date_filter == 'past':
        events = events.filter(date__lt=timezone.now())
    
    # Get filter options
    event_types = Event.EVENT_TYPES
    cities = Event.objects.values_list('city', flat=True).distinct().order_by('city')
    
    context = {
        'events': events,
        'event_types': event_types,
        'cities': cities,
        'filters': {
            'event_type': event_type,
            'city': city,
            'date_filter': date_filter,
        }
    }
    return render(request, 'events/event_list.html', context)


def event_detail(request, slug):
    """Detail view for an event"""
    event = get_object_or_404(Event, slug=slug, is_active=True)
    related_events = Event.objects.filter(
        is_active=True,
        city=event.city
    ).exclude(id=event.id)[:3]
    
    context = {
        'event': event,
        'related_events': related_events,
    }
    return render(request, 'events/event_detail.html', context)