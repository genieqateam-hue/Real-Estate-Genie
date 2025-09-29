from django.shortcuts import render, get_object_or_404
from .models import SaleProperty


def sale_list(request):
    """List all sale properties with filtering"""
    properties = SaleProperty.objects.filter(is_sold=False)
    
    # Filtering
    property_type = request.GET.get('property_type')
    city = request.GET.get('city')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    bedrooms = request.GET.get('bedrooms')
    investment_potential = request.GET.get('investment_potential')
    
    if property_type:
        properties = properties.filter(property_type=property_type)
    if city:
        properties = properties.filter(city__icontains=city)
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)
    if bedrooms:
        properties = properties.filter(bedrooms=bedrooms)
    if investment_potential:
        properties = properties.filter(investment_potential=investment_potential)
    
    # Get filter options
    property_types = SaleProperty.PROPERTY_TYPES
    cities = SaleProperty.objects.values_list('city', flat=True).distinct().order_by('city')
    investment_options = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    
    context = {
        'properties': properties,
        'property_types': property_types,
        'cities': cities,
        'investment_options': investment_options,
        'filters': {
            'property_type': property_type,
            'city': city,
            'min_price': min_price,
            'max_price': max_price,
            'bedrooms': bedrooms,
            'investment_potential': investment_potential,
        }
    }
    return render(request, 'sale/sale_list.html', context)


def sale_detail(request, slug):
    """Detail view for a sale property"""
    property = get_object_or_404(SaleProperty, slug=slug, is_sold=False)
    related_properties = SaleProperty.objects.filter(
        is_sold=False,
        city=property.city
    ).exclude(id=property.id)[:3]
    
    context = {
        'property': property,
        'related_properties': related_properties,
    }
    return render(request, 'sale/sale_detail.html', context)
