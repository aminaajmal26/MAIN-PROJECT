
from django import forms
from .models import Appointment
from User_app.models import Doctor

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = [
            'name',
            'contact_number',
            'email',
            'gender',
            'location',
            'specialization',
            'user',
            'appointment_date',
            'appointment_time',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name'
            }),
            'contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contact Number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Location'
            }),
            'specialization': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Specialization'
            }),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'appointment_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'appointment_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            }),
        }
