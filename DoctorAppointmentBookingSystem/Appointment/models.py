from django.db import models
from User_app.models import Doctor  # Import Doctor from the user app
from django.contrib.auth.models import User
GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Completed', 'Completed'),
]

class Appointment(models.Model):
    # Patient / Visitor info

    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    name = models.CharField(max_length=100) 
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    location = models.CharField(max_length=200)

    # Appointment info
    specialization = models.CharField(max_length=100)
    user = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # Link to Doctor from user app
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (f"{self.name} ({self.patient.username}) → "f"Dr. {self.user.user.username} "
        f"on {self.appointment_date} at "
        f"{self.appointment_time.strftime('%I:%M %p')}"
    )

