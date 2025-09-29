from django.db import models
from django.utils.text import slugify


class RentProperty(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('condo', 'Condo'),
        ('townhouse', 'Townhouse'),
        ('studio', 'Studio'),
        ('loft', 'Loft'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    square_feet = models.PositiveIntegerField()
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    image = models.ImageField(upload_to='rent_properties/')
    is_featured = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Investment metrics
    annual_rental_yield = models.DecimalField(max_digits=5, decimal_places=2, help_text="Annual rental yield percentage")
    cap_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text="Capitalization rate percentage")
    cash_flow = models.DecimalField(max_digits=10, decimal_places=2, help_text="Monthly cash flow")
    roi = models.DecimalField(max_digits=5, decimal_places=2, help_text="Return on investment percentage")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Rent Property'
        verbose_name_plural = 'Rent Properties'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


