from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'order', 'is_active', 'created_at']
    list_filter = ['role', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['order', 'is_active']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'role', 'description', 'image')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url'),
            'classes': ('collapse',)
        }),
        ('Additional Social Links', {
            'fields': ('social_links',),
            'classes': ('collapse',)
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
    )
