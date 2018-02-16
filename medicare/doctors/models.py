from django.db import models
from datetime import date, datetime, time, timedelta
# Create your models here.
class History(models.Model):
    PRESCRIPTION = (
        ('y', 'yes'),
        ('n', 'no')
    )
    appointment = models.OneToOneField('CompleteAppointment', on_delete=models.CASCADE)
    prescription = models.CharField(max_length=1, choices=PRESCRIPTION,)
    prescribed = models.CharField(max_length=150)
    record_date = models.DateTimeField(auto_now=datetime)
    visit_record = models.TextField()

    def __str__(self):
        return str(self.appointment)

class CompleteAppointment(models.Model):
    patient = models.ForeignKey('records.Patient', on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    visit_reason = models.CharField(max_length=150)
    doctor = models.ForeignKey('employees.Doctor', on_delete=models.CASCADE, default='none')

    class Meta:
        ordering = ('appointment_date','appointment_time',)