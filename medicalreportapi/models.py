from django.db import models
from doctorapi.models import Doctor
from patientapi.models import Patient

# Create your models here.
class MedicalReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    prescription = models.TextField()
    treatment_plan = models.TextField()
    visit_date = models.DateField()
    
    