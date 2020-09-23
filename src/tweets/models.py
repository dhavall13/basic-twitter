from django.db import models

# Create your models here.
class Tweet(models.Model):
    
    #id = 
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/',max_length=200, blank=True, null=True)
    