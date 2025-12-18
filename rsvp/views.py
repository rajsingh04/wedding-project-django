from django.shortcuts import render, redirect
from django.contrib import messages
from .models import RSVP, ContactInfo
from .forms import RSVPForm

def rsvp_view(request):
    contact_info = ContactInfo.objects.first()
    
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your RSVP!')
            return redirect('rsvp')
    else:
        form = RSVPForm()
    
    return render(request, 'rsvp/rsvp.html', {
        'form': form,
        'contact_info': contact_info
    })
