from django.shortcuts import render
from sale.models import SaleProperty
from rent.models import RentProperty
from events.models import Event

def home(request):
    """Home page view"""
    sales = SaleProperty.objects.filter(is_sold=False)[:3]  # Get a few for the home page
    rents = RentProperty.objects.filter(is_available=True)[:3]
    events = Event.objects.filter(is_active=True)[:3]
    context = {
        'sales': sales,
        'rents': rents,
        'events': events,
    }
    return render(request, 'home.html', context)