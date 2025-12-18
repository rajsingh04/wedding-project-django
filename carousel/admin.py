from django.contrib import admin
from .models import CarouselSlide

@admin.register(CarouselSlide)
class CarouselSlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'subtitle']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {}
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle', 'description', 'image')
        }),
        ('Button', {
            'fields': ('button_text', 'button_link')
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
    )
