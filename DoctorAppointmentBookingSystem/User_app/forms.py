from django import forms
from django.contrib.auth.models import User
from .models import Doctor


class DoctorRegistrationForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Doctor
        fields = [
            'designation',
            'specialization',
            'experience',
            'education',
            'expertise',
            'languages',
            'photo'
        ]

    def save(self, commit=True):
        # create user
        user = User.objects.create_user(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )

        # create doctor
        doctor = super().save(commit=False)
        doctor.user = user

        if commit:
            doctor.save()

        return doctor




