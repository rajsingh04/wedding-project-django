from django.db import models

class Couple(models.Model):
    ROLE_CHOICES = [
        ('bride', 'Bride'),
        ('groom', 'Groom'),
    ]
    
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='couple/', default='static/img/bride.jpg')
    social_links = models.JSONField(default=dict, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Couple Member'
        verbose_name_plural = 'Couple Members'
    
    def __str__(self):
        return f"{self.name} - {self.role}"

class About(models.Model):
    wedding_date = models.DateField()
    wedding_venue = models.CharField(max_length=200, default='Wedding Venue')
    relationship_years = models.PositiveIntegerField(default=2)
    love_story_summary = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

    def __str__(self):
        return f'Wedding Details - {self.wedding_date}'
