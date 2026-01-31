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
from . import views

# appointment/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book_appointment',views.book_appointment,name='book_appointment'),
    path('load_doctors/',views.load_doctors,name='load_doctors'),  # AJAX URL
    path('appointment_history', views.appointment_history, name='appointment_history'),
    path('confirm_appointment',views.confirm_appointment,name="confirm_appointment") 
 ]
