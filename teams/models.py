from django.db import models

# Create your models here.
class Teams(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
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