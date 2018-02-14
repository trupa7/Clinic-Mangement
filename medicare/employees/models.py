from django.db import models

# Create your models here.

class Employee(models.Model):
    SL = (
<<<<<<< HEAD
        ('DO', 'Doctor'),
        ('RE', 'Receptionist'),
        ('NU', 'Nurse'),
        ('PH', 'Pharmacist'),
        ('LA', 'Lab Technician'),
        
=======
        ('Dr.', 'Doctor'),
        ('Front Desk', 'Front Desk'),
        ('Nurse', 'Nurse')
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
        )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
<<<<<<< HEAD
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
        

=======
    specialty_label = models.CharField(max_length=10, choices=SL)

    def __str__(self):
        return '{}, {} {}'.format(self.specialty_label, self.first_name, self.last_name)



class Account(models.Model):


    user = models.OneToOneField('Employee', on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type_label = models.CharField(max_length=100)
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
