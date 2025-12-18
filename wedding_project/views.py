from django.shortcuts import render, redirect
from carousel.models import CarouselSlide
from about.models import Couple, About
from story.models import StoryEvent
from timeline.models import TimelineEvent
from gallery.models import GalleryImage, GalleryCategory
from team.models import TeamMember
from rsvp.models import RSVP, ContactInfo, WeddingEvent

def home_page(request):
    slides = CarouselSlide.objects.filter(is_active=True).order_by('order')
    context = {
        'slides': slides
    }
    return render(request, 'home.html', context)

def about_page(request):
    couple_members = Couple.objects.filter(is_active=True)
    about_info = About.objects.filter(is_active=True).first()
    bride = couple_members.filter(role='bride').first()
    groom = couple_members.filter(role='groom').first()
    
    context = {
        'bride': bride,
        'groom': groom,
        'about_info': about_info,
        'couple_members': couple_members
    }
    return render(request, 'about.html', context)

def story_page(request):
    story_events = StoryEvent.objects.filter(is_active=True).order_by('order')
    featured_events = story_events.filter(is_featured=True)
    
    context = {
        'story_events': story_events,
        'featured_events': featured_events
    }
    return render(request, 'story.html', context)

def timeline_page(request):
    timeline_events = TimelineEvent.objects.filter(is_active=True).order_by('order')
    
    context = {
        'timeline_events': timeline_events
    }
    return render(request, 'timeline.html', context)

def gallery_page(request):
    gallery_images = GalleryImage.objects.filter(is_active=True).order_by('order')
    categories = GalleryCategory.objects.filter(is_active=True)
    featured_images = gallery_images.filter(is_featured=True)
    
    context = {
        'gallery_images': gallery_images,
        'categories': categories,
        'featured_images': featured_images
    }
    return render(request, 'gallery.html', context)

def team_page(request):
    team_members = TeamMember.objects.filter(is_active=True).order_by('role', 'order')
    bridesmaids = team_members.filter(role__in=['bridesmaid', 'maid_of_honor'])
    groomsmen = team_members.filter(role__in=['groomsman', 'best_man'])
    
    context = {
        'team_members': team_members,
        'bridesmaids': bridesmaids,
        'groomsmen': groomsmen
    }
    return render(request, 'team.html', context)

def rsvp_page(request):
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    wedding_events = WeddingEvent.objects.filter(is_active=True).order_by('date')
    
    context = {
        'contact_info': contact_info,
        'wedding_events': wedding_events
    }
    return render(request, 'rsvp.html', context)