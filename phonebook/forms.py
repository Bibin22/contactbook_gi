from django import forms
from django.forms import ModelForm
from .models import *



class ContactForm(ModelForm):
    class Meta:
        model = ContactBook
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true',
                                           'pattern': '^[a-zA-Z_ ]*$',
                                           'title': 'Name should only contain letters'
                                           }),
            'phone_no': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'type': 'text',
                                                 'pattern': '[0-9]{6,11}',
                                                 'title': 'Phone number Should be 6-12 digits and accept only digits'
                                                 }),

        }