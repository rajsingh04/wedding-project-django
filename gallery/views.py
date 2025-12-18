from django.shortcuts import render
from .models import GalleryImage, GalleryCategory

def gallery_view(request):
    gallery_images = GalleryImage.objects.filter(is_active=True).order_by('order')
    categories = GalleryCategory.objects.filter(is_active=True)
    featured_images = gallery_images.filter(is_featured=True)
    
    context = {
        'gallery_images': gallery_images,
        'categories': categories,
        'featured_images': featured_images
    }
    return render(request, 'gallery.html', context)
