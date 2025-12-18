from django.db import models

class CarouselSlide(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='carousel/', default='static/img/carousel-1.jpg')
    button_text = models.CharField(max_length=50, default='Book Now')
    button_link = models.CharField(max_length=200, default='/rsvp/')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Carousel Slide'
        verbose_name_plural = 'Carousel Slides'
    
    def __str__(self):
        return self.title
