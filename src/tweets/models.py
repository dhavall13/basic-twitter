import random
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
   # TODO : 
   # null = True, on_ del =set null (this tweets is deleted) in user
    #id = models.Auto
     
    user = models.ForeignKey(User, on_delete=models.CASCADE ) # many users can tweet 
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    # def __str__(self):
    #     return self.content
    class Meta:
        ordering = ['-id']
    
    def serialize(self):
        return {
            "id": self.id,
            "content":self.content,
            "likes": random.randint(0, 100)
        }