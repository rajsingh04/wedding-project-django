from django.contrib import admin
from .models import GalleryCategory, GalleryImage

@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_active']

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order', 'is_featured', 'is_active', 'uploaded_at']
    list_filter = ['category', 'is_featured', 'is_active', 'uploaded_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_featured', 'is_active']
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'description', 'image', 'thumbnail')
        }),
        ('Organization', {
            'fields': ('category', 'order')
        }),
        ('Settings', {
            'fields': ('is_featured', 'is_active')
        }),
    )
