from django.contrib import admin
from .models import StoryEvent

@admin.register(StoryEvent)
class StoryEventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'order', 'is_featured', 'is_active', 'created_at']
    list_filter = ['date', 'is_featured', 'is_active']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_featured', 'is_active']
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'description', 'date', 'image')
        }),
        ('Settings', {
            'fields': ('order', 'is_featured', 'is_active')
        }),
    )
