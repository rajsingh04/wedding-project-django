from django.shortcuts import render
from .models import Couple, About

def about_view(request):
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
