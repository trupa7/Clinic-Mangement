from django.db import models

# Create your models here.
class Prescription(models.Model):
    patient_id = models.ForeignKey('records.Patient',on_delete=models.CASCADE)
    drug_name = models.CharField(max_length=20)
    prescription_date=models.DateField()
    prescribedBy = models.ForeignKey('employees.Employee',on_delete=models.CASCADE)

class Pharmacist(models.Model):
    name = models.CharField(max_length=20)
    prescription_id=models.ForeignKey('Prescription',on_delete=models.CASCADE)
