from django.db import models

class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('bridesmaid', 'Bridesmaid'),
        ('groomsman', 'Groomsman'),
        ('maid_of_honor', 'Maid of Honor'),
        ('best_man', 'Best Man'),
        ('flower_girl', 'Flower Girl'),
        ('ring_bearer', 'Ring Bearer'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='team/', default='static/img/team-1.jpg')
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    social_links = models.JSONField(default=dict, blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['role', 'order']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
    
    def __str__(self):
        return f"{self.name} - {self.get_role_display()}"
