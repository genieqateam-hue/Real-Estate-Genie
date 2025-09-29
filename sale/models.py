from django.db import models
from django.utils.text import slugify


class SaleProperty(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('condo', 'Condo'),
        ('townhouse', 'Townhouse'),
        ('villa', 'Villa'),
        ('penthouse', 'Penthouse'),
        ('commercial', 'Commercial'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    square_feet = models.PositiveIntegerField()
    lot_size = models.DecimalField(max_digits=10, decimal_places=2, help_text="Lot size in square feet")
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    image = models.ImageField(upload_to='sale_properties/')
    is_featured = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Investment metrics
    price_per_sqft = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per square foot")
    appreciation_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text="Annual appreciation rate percentage")
    market_value = models.DecimalField(max_digits=12, decimal_places=2, help_text="Current market value")
    investment_potential = models.CharField(max_length=20, choices=[
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ], default='medium')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Sale Property'
        verbose_name_plural = 'Sale Properties'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.square_feet and self.price:
            self.price_per_sqft = self.price / self.square_feet
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


