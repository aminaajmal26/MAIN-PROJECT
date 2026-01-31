from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(default=0)
    education = models.CharField(max_length=200, blank=True)

    expertise = models.TextField(blank=True, help_text="One per line")
    languages = models.TextField(blank=True, help_text="One per line")
    
    photo = models.ImageField(upload_to='doctors/', blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


