from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Doctor(models.Model):
    dr_name = models.CharField(max_length=100)
    dr_specialization = models.CharField(max_length=100)
    dr_experience = models.PositiveIntegerField()
    dr_availability = models.BooleanField()
    dr_contact = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Contact number must be exactly 10 digits.',
                code='invalid_contact'
            )
        ]
    )    
    def __str__(self):
        return f"{self.dr_name}, {self.dr_specialization}, {self.dr_experience}, {self.dr_availability}, {self.dr_contact}"
