from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Patient(models.Model):
    pname = models.CharField(max_length=100)
    page = models.PositiveBigIntegerField()
    pgender = models.CharField(max_length=15)
    paddress = models.CharField(max_length=200)
    pcontact = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Contact number must be exactly 10 digits.',
                code='invalid_contact'
            )
        ]
    )    
    pdate = models.DateField(auto_now_add=True)
    pmed_his = models.TextField()
    pcurrent_med = models.TextField()
    pallergies = models.TextField()
    pmedication = models.TextField()
    
    def __str__(self):
        return f"{self.pname}, {self.page}, {self.pgender}, {self.paddress}, {self.pcontact}, {self.pdate}, {self.pmed_his}, {self.pcurrent_med}, {self.pallergies}, {self.pmedication}"
    