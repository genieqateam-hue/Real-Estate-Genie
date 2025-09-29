from django.contrib import admin
from .models import PageWidget

@admin.register(PageWidget)
class PageWidgetAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'page', 'is_active', 'created_at']
    list_filter = ['page', 'is_active', 'created_at']
    search_fields = ['script_content']
    list_editable = ['is_active']
    ordering = ['page']
    
    fieldsets = (
        ('Widget Information', {
            'fields': ('script_content',)
        }),
        ('Page Assignment', {
            'fields': ('page', 'is_active')
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('page')