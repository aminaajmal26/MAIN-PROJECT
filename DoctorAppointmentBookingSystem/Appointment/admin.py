from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'patient',
        'get_doctor_name',
        'specialization',
        'appointment_date',
        'appointment_time',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'appointment_date',
        'specialization',
    )

    search_fields = (
        'name',
        'patient__username',
        'patient__email',
        'user__user__username',
        'specialization',
    )

    ordering = ('-created_at',)

    def get_doctor_name(self, obj):
        return obj.user.user.username

    get_doctor_name.short_description = 'Doctor'
