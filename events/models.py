from django.db import models
from django.utils.text import slugify


class Event(models.Model):
    EVENT_TYPES = [
        ('investment_seminar', 'Investment Seminar'),
        ('property_tour', 'Property Tour'),
        ('networking', 'Networking Event'),
        ('workshop', 'Workshop'),
        ('conference', 'Conference'),
        ('webinar', 'Webinar'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    image = models.ImageField(upload_to='events/')
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    max_attendees = models.PositiveIntegerField(blank=True, null=True)
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Investment focus
    target_audience = models.CharField(max_length=100, help_text="Target investor audience")
    investment_focus = models.CharField(max_length=200, help_text="Investment topics covered")
    speaker_name = models.CharField(max_length=100, blank=True)
    speaker_title = models.CharField(max_length=100, blank=True)
    
    class Meta:
        ordering = ['date']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    @property
    def is_upcoming(self):
        from django.utils import timezone
        return self.date > timezone.now()
    
    @property
    def is_past(self):
        from django.utils import timezone
        return self.date < timezone.now()