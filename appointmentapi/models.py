from django.db import models
from patientapi.models import Patient
from doctorapi.models import Doctor
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    apmt_date = models.DateField()
    apmt_time = models.TimeField()
    apmt_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')])
