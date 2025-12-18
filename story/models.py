from django.db import models

class StoryEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='story/', default='static/img/story-1.jpg')
    order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Story Event'
        verbose_name_plural = 'Story Events'
    
    def __str__(self):
        return self.title
