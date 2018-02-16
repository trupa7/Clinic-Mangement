from django.db import models
from django.utils import timezone
from records.models import Patient

# Create your models here.
class Nurses(models.Model):
    patient_id = models.ForeignKey('records.Patient', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default = timezone.now)
    details=models.TextField()
    
    def __str__(self):
        return str(self.patient_id)