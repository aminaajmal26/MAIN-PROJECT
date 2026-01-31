from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm
from User_app.models import Doctor



@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user  # 🔥 VERY IMPORTANT
            appointment.save()
            messages.success(request, 'Appointment booked successfully')
            return redirect('appointment_history')
    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})



from django.http import JsonResponse
from User_app.models import Doctor

def load_doctors(request):
    specialization = request.GET.get('specialization')

    if specialization:
        doctors = Doctor.objects.filter(
            specialization__icontains=specialization
        )
    else:
        doctors = Doctor.objects.none()

    data = [
        {
            'id': doctor.id,
            'name': doctor.user.username
        }
        for doctor in doctors
    ]

    return JsonResponse(data, safe=False)



# # appointment/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment

@login_required
def appointment_history(request):
    appointments = Appointment.objects.filter(
        patient=request.user
    ).order_by('-appointment_date')

    return render(request, 'appointment_history.html', {
        'appointments': appointments
    })


@login_required
def confirm_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.status = 'Confirmed'
    appointment.save()
    return redirect('appointment_history')

# @login_required
# def doctor_appointments(request):
#     appointments = Appointment.objects.filter(
#         user__user=request.user
#     ).order_by('-appointment_date')

#     return render(request, 'doctor_appointments.html', {
#         'appointments': appointments
#     })


