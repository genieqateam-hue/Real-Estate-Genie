from django.contrib import admin
from .models import SaleProperty


@admin.register(SaleProperty)
class SalePropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'property_type', 'price', 'bedrooms', 'bathrooms', 'city', 'is_featured', 'is_sold', 'created_at']
    list_filter = ['property_type', 'is_featured', 'is_sold', 'city', 'investment_potential', 'created_at']
    search_fields = ['title', 'description', 'address', 'city']
    list_editable = ['is_featured', 'is_sold']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'property_type')
        }),
        ('Property Details', {
            'fields': ('price', 'bedrooms', 'bathrooms', 'square_feet', 'lot_size', 'address', 'city', 'state', 'zip_code')
        }),
        ('Investment Metrics', {
            'fields': ('price_per_sqft', 'appreciation_rate', 'market_value', 'investment_potential'),
            'classes': ('collapse',)
        }),
        ('Status & Media', {
            'fields': ('image', 'is_featured', 'is_sold')
        }),
    )
