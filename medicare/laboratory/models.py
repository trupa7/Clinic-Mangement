from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_id = models.CharField(max_length=5,primary_key=True)
    patient_name=models.CharField(max_length=20)

class Doctor(models.Model):
    doctor_id = models.CharField(max_length=5,primary_key=True)
    doctor_name = models.CharField(max_length=20)

class Laboratory(models.Model):
    test_id = models.CharField(max_length=5)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_date = models.DateTimeField()
    test_details = models.TextField()
    result_status = models.CharField(max_length=10)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)



