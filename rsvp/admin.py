from django.contrib import admin
from .models import RSVP, ContactInfo, WeddingEvent

@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'response', 'number_of_guests', 'meal_preference', 'created_at']
    list_filter = ['response', 'meal_preference', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Guest Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Response Details', {
            'fields': ('response', 'number_of_guests', 'meal_preference')
        }),
        ('Special Requirements', {
            'fields': ('dietary_requirements', 'special_requests', 'message')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['venue_name', 'phone', 'email', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['venue_name', 'address']

@admin.register(WeddingEvent)
class WeddingEventAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'location', 'is_main_event', 'is_active']
    list_filter = ['is_main_event', 'is_active', 'date']
    search_fields = ['name', 'location', 'description']
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Event Details', {
            'fields': ('name', 'date', 'location', 'address')
        }),
        ('Additional Info', {
            'fields': ('description', 'dress_code', 'map_url')
        }),
        ('Settings', {
            'fields': ('is_main_event', 'is_active')
        }),
    )
