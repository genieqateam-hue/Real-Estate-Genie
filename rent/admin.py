from django.contrib import admin
from .models import RentProperty


@admin.register(RentProperty)
class RentPropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'property_type', 'monthly_rent', 'bedrooms', 'bathrooms', 'city', 'is_featured', 'is_available', 'created_at']
    list_filter = ['property_type', 'is_featured', 'is_available', 'city', 'created_at']
    search_fields = ['title', 'description', 'address', 'city']
    list_editable = ['is_featured', 'is_available']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'property_type')
        }),
        ('Property Details', {
            'fields': ('monthly_rent', 'bedrooms', 'bathrooms', 'square_feet', 'address', 'city', 'state', 'zip_code')
        }),
        ('Investment Metrics', {
            'fields': ('annual_rental_yield', 'cap_rate', 'cash_flow', 'roi'),
            'classes': ('collapse',)
        }),
        ('Status & Media', {
            'fields': ('image', 'is_featured', 'is_available')
        }),
    )
