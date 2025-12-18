from django.db import models

class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Gallery Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery/', default='static/img/gallery-1.jpg')
    thumbnail = models.ImageField(upload_to='gallery/thumbnails/', blank=True)
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-uploaded_at']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'
    
    def __str__(self):
        return self.title or f"Gallery Image {self.id}"
