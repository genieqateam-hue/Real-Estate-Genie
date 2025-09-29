from django.shortcuts import render, get_object_or_404
from .models import RentProperty


def rent_list(request):
    """List all rent properties with filtering"""
    properties = RentProperty.objects.filter(is_available=True)
    
    # Filtering
    property_type = request.GET.get('property_type')
    city = request.GET.get('city')
    min_rent = request.GET.get('min_rent')
    max_rent = request.GET.get('max_rent')
    bedrooms = request.GET.get('bedrooms')
    
    if property_type:
        properties = properties.filter(property_type=property_type)
    if city:
        properties = properties.filter(city__icontains=city)
    if min_rent:
        properties = properties.filter(monthly_rent__gte=min_rent)
    if max_rent:
        properties = properties.filter(monthly_rent__lte=max_rent)
    if bedrooms:
        properties = properties.filter(bedrooms=bedrooms)
    
    # Get filter options
    property_types = RentProperty.PROPERTY_TYPES
    cities = RentProperty.objects.values_list('city', flat=True).distinct().order_by('city')
    
    context = {
        'properties': properties,
        'property_types': property_types,
        'cities': cities,
        'filters': {
            'property_type': property_type,
            'city': city,
            'min_rent': min_rent,
            'max_rent': max_rent,
            'bedrooms': bedrooms,
        }
    }
    return render(request, 'rent/rent_list.html', context)


def rent_detail(request, slug):
    """Detail view for a rent property"""
    property = get_object_or_404(RentProperty, slug=slug, is_available=True)
    related_properties = RentProperty.objects.filter(
        is_available=True,
        city=property.city
    ).exclude(id=property.id)[:3]
    
    context = {
        'property': property,
        'related_properties': related_properties,
    }
    return render(request, 'rent/rent_detail.html', context)
