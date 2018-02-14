from django.db import models
from django.utils import timezone
# Create your models here.

class Laboratory(models.Model):
    STATUS= (
        ('P', 'Pending'),
        ('S', 'Started'),
        ('C', 'Completed')
    )
    
    test_id = models.CharField(max_length=5)
    patient_id = models.ForeignKey('records.Patient', on_delete=models.CASCADE)
    test_date = models.DateTimeField(default = timezone.now)
    test_details = models.TextField(null=True)
    result_status = models.CharField(max_length=10,choices=STATUS,null=True)
    doctor_id = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)

    def get_pID(self):
        return self.patient_id_id

