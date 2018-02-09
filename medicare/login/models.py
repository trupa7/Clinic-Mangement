from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.context_processors import auth
from django.utils import timezone
# Create your models here.
class AllUser(models.Model):
    username=models.CharField(max_length=200)
    password1=models.CharField(max_length=200)
    label=models.CharField(max_length=200)
    
    
    
    
    