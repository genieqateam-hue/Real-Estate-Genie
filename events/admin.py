from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'date', 'location', 'city', 'is_featured', 'is_active', 'registration_fee']
    list_filter = ['event_type', 'is_featured', 'is_active', 'city', 'date']
    search_fields = ['title', 'description', 'location', 'city', 'speaker_name']
    list_editable = ['is_featured', 'is_active']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'event_type')
        }),
        ('Event Details', {
            'fields': ('date', 'end_date', 'location', 'city', 'state', 'max_attendees', 'registration_fee')
        }),
        ('Investment Focus', {
            'fields': ('target_audience', 'investment_focus', 'speaker_name', 'speaker_title'),
            'classes': ('collapse',)
        }),
        ('Status & Media', {
            'fields': ('image', 'is_featured', 'is_active')
        }),
    )