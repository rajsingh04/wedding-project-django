from django.db import models

class RSVP(models.Model):
    RESPONSE_CHOICES = [
        ('yes', 'Yes, I will attend'),
        ('no', 'No, I cannot attend'),
        ('maybe', 'Maybe'),
    ]
    
    MEAL_CHOICES = [
        ('vegetarian', 'Vegetarian'),
        ('non_vegetarian', 'Non-Vegetarian'),
        ('vegan', 'Vegan'),
        ('gluten_free', 'Gluten Free'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    response = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    number_of_guests = models.IntegerField(default=1)
    meal_preference = models.CharField(max_length=20, choices=MEAL_CHOICES, blank=True)
    dietary_requirements = models.TextField(blank=True)
    special_requests = models.TextField(blank=True)
    message = models.TextField(blank=True, help_text='Special message for the couple')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'RSVP Response'
        verbose_name_plural = 'RSVP Responses'
    
    def __str__(self):
        return f"{self.name} - {self.get_response_display()}"

class ContactInfo(models.Model):
    venue_name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    map_embed_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"
    
    def __str__(self):
        return self.venue_name

class WeddingEvent(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=300)
    address = models.TextField()
    map_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    dress_code = models.CharField(max_length=100, blank=True)
    is_main_event = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
        verbose_name = 'Wedding Event'
        verbose_name_plural = 'Wedding Events'

    def __str__(self):
        return self.name
