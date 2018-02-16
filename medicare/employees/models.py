from django.db import models

# Create your models here.

class Employee(models.Model):
    SL = (
        ('DO', 'Doctor'),
        ('RE', 'Receptionist'),
        ('NU', 'Nurse'),
        ('PH', 'Pharmacist'),
        ('LA', 'Lab Technician'),
        
        )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    type_label=models.CharField(max_length=200,choices=SL)
    speciality_label=models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.username
    
    def getType(self):
        return self.type_label
    
    def getSpec(self):
        return self.speciality_label
    
#   def getDoctor(self):
#        if 'DO' in self.type_label:
#            return self.username
#         


class Doctor(models.Model):

    username=models.CharField(max_length=200)

    
    def __str__(self):
        return self.username
    
   
