from django.db import models

class TimelineEvent(models.Model):
    EVENT_TYPES = [
        ('ceremony', 'Wedding Ceremony'),
        ('reception', 'Reception'),
        ('photoshoot', 'Photo Shoot'),
        ('dinner', 'Dinner'),
        ('party', 'After Party'),
        ('other', 'Other')
    ]

    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='other')
    description = models.TextField()
    date = models.DateField(blank=True, null=True)
    time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    icon = models.CharField(max_length=50, help_text='FontAwesome icon class', default='fa fa-heart')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Timeline Event'
        verbose_name_plural = 'Timeline Events'
    
    def __str__(self):
        return f"{self.title} - {self.time}"
