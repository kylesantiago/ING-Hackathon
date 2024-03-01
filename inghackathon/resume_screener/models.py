from django.db import models
from django.db.models import Model 
  
class Applicants(Model): 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    resume = models.FileField(null=True,blank=True, upload_to='') 
