from django.db import models
from django.db.models import Model 
  
class Applicants(Model): 
    resume = models.FileField(null=True,blank=True, upload_to='') 

class JobOpening(Model):
    job_title = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=255)
    job_Category = models.CharField(max_length=255)
    certifications = models.TextField()
    experience = models.TextField()
    keywords = models.TextField()
    job_description = models.TextField()
    skills = models.TextField()
    education = models.TextField()


class Results(Model):
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    score = models.IntegerField()