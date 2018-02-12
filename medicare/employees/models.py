from django.db import models

# Create your models here.

class Employee(models.Model):
    SL = (
        ('dr', 'Doctor'),
        ('fd', 'Front Desk'),
        ('nr', 'Nurse')
        )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty_label = models.CharField(max_length=10, choices=SL)

    def __str__(self):
        return '{}, {} {}'.format(self.specialty_label, self.first_name, self.last_name)



class Account(models.Model):


    user = models.OneToOneField('Employee', on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type_label = models.CharField(max_length=100)
