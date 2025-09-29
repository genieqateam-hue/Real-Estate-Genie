from django.db import models

class PageWidget(models.Model):
    """Model to store custom widgets/scripts added by admin for specific pages"""
    
    PAGE_CHOICES = [
        ('home', 'Home Page'),
        ('rent', 'Rent Properties'),
        ('sale', 'Sale Properties'),
        ('events', 'Events'),
    ]
    
    script_content = models.TextField(verbose_name="Script", help_text="The script tag content to append to the page")
    page = models.CharField(max_length=20, choices=PAGE_CHOICES, help_text="Which page this widget appears on")
    is_active = models.BooleanField(default=True, help_text="Whether this widget is active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['page']
        verbose_name = 'Page Widget'
        verbose_name_plural = 'Page Widgets'
    
    def __str__(self):
        return f"{self.get_page_display()}: Widget {self.id}"