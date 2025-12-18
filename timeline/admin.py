from django.contrib import admin
from .models import TimelineEvent

@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'date', 'time', 'location', 'order', 'is_active']
    list_filter = ['event_type', 'date', 'is_active']
    search_fields = ['title', 'description', 'location']
    list_editable = ['order', 'is_active']
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Event Details', {
            'fields': ('title', 'event_type', 'description')
        }),
        ('Schedule', {
            'fields': ('date', 'time', 'end_time', 'location')
        }),
        ('Display', {
            'fields': ('icon', 'order', 'is_active')
        }),
    )
