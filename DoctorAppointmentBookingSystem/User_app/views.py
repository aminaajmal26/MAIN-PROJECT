from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 
# from Admin_app.models import *
from django.http import HttpResponse


# Create your views here.

  #  REGISTER USER

def Register_user(request):
    if request.method=="POST":
        username=request.POST['username']
        email = request.POST['email'] 
        password = request.POST['password'] 
        confirm_password = request.POST['confirm_password']  
        if password != confirm_password: 
           return render(request, 'register.html', {'error': 'Passwords do not match!'}) 
        if User.objects.filter(username=username).exists(): 
          return render(request, 'register.html', {'error': 'Username already taken!'})
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect('login_user')
    return render(request, 'register.html')

#   LOGIN uSER

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password!")
            return render(request, 'login.html')

    return render(request, 'login.html')

@login_required(login_url='login_user')
def dashboard(request):
    return render(request,'dashboard.html')


#    LOGOUT USER


# def logout_user(request):
#     logout(request) 
#     return redirect('login_user')


def logout_user(request):
    logout(request) 
    return render(request,'logout.html')

        # DOCTOR MODEL VIEWS

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Doctor

@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

def homepage(request):
    return render(request, 'careconnect.html')


def about_us(request):
    return render(request, 'about_us.html')


def contact_us(request):
    return render(request, 'contact_us.html')

# user/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DoctorRegistrationForm


@login_required
def add_doctor_details(request):

    if request.method == 'POST':
        # 👉 PASTE IT HERE
        form = DoctorRegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = request.user
            doctor.save()
            return redirect('dashboard')

    else:
        form = DoctorRegistrationForm()

    return render(request, 'add_doctor.html', {'form': form})



# doctor/views.py

from django.shortcuts import render, get_object_or_404
from .models import Doctor

def doctor_profile(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    return render(request, 'doctor_profile.html', {'doctor': doctor})



# specialization/views.py
from django.shortcuts import render
from .models import Doctor

SPECIALIZATIONS = [
    "Urology",
    "Gynecology",
    "Cardiology",
    "Orthopedics",
    "Neurology",
    "Pediatrics",
    "Dermatology",
    "ENT",
    "General Medicine",
    "Oncology",
]

def specialization_list(request):
    return render(
        request,
        'specialization_list.html',
        {'specializations': SPECIALIZATIONS}
    )



def doctor_by_specialization(request, specialization):
    doctors = Doctor.objects.filter(
        specialization__iexact=specialization
    )

    return render(
        request,
        'doctor_list.html',
        {
            'doctors': doctors,
            'selected_specialization': specialization
        }
    )
