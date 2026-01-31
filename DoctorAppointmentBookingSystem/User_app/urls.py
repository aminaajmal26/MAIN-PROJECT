"""
URL configuration for DoctorAppointmentBookingSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('Register_user',views.Register_user,name="Register_user"),
    path('login_user',views.login_user,name="login_user"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout_user',views.logout_user,name="logout_user"),
    path('doctors/',views.doctor_list,name='doctor_list'),
    path('homepage',views.homepage,name="homepage"),
    path('about_us/',views.about_us,name='about_us'),
     path('contact_us/',views.contact_us,name='contact_us'),
    path('add_doctor_details',views.add_doctor_details,name="add_doctor_details"),
    path('doctor/<int:id>/',views.doctor_profile, name='doctor_profile'),
    path('specialization_list', views.specialization_list, name='specialization_list'),
    path('doctors/<str:specialization>/',views.doctor_by_specialization,name='doctor_by_specialization'),
    
]
