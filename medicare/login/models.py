from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.context_processors import auth
from django.utils import timezone
# Create your models here.
class AllUser(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    type_label=models.CharField(max_length=200)
    speciality_label=models.CharField(max_length=200)
    
    def __str__(self):
        return self.username
    
    def getType(self):
        return self.type_label
    
    def getSpec(self):
        return self.speciality_label
        
    
    