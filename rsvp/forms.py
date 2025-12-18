from django import forms
from .models import RSVP

class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['name', 'email', 'phone', 'response', 'number_of_guests', 'dietary_requirements', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone'}),
            'response': forms.Select(attrs={'class': 'form-control'}),
            'number_of_guests': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'dietary_requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any dietary requirements...'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your message...'})
        }