from django.contrib import admin
from .models import Couple, About

@admin.register(Couple)
class CoupleAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'is_active', 'created_at']
    list_filter = ['role', 'is_active']
    search_fields = ['name', 'description']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'role', 'description', 'image')
        }),
        ('Social Links', {
            'fields': ('social_links',),
            'classes': ('collapse',)
        }),
        ('Settings', {
            'fields': ('is_active',)
        }),
    )

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['wedding_date', 'wedding_venue', 'relationship_years', 'is_active']
    list_filter = ['wedding_date', 'is_active']
    search_fields = ['wedding_venue', 'love_story_summary']
    
    fieldsets = (
        ('Wedding Details', {
            'fields': ('wedding_date', 'wedding_venue', 'relationship_years')
        }),
        ('Story', {
            'fields': ('love_story_summary',)
        }),
        ('Settings', {
            'fields': ('is_active',)
        }),
    )
