from django.db import models
from datetime import date, datetime, time

# Create your models here.
class Prescription(models.Model):
    patient_id = models.ForeignKey('records.Patient',on_delete=models.CASCADE)
    drug_name = models.CharField(max_length=20)
    prescription_date=models.DateField(auto_now=datetime)
    prescribedBy = models.ForeignKey('employees.Doctor',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

class Pharmacist(models.Model):
    name =models.ForeignKey('employees.Doctor',on_delete=models.CASCADE)
    prescription_id=models.ForeignKey('Prescription',on_delete=models.CASCADE)
