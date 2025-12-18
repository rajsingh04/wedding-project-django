from django.shortcuts import render
from .models import CarouselSlide

def home_view(request):
    slides = CarouselSlide.objects.filter(is_active=True)
    return render(request, 'carousel/home.html', {'slides': slides})
