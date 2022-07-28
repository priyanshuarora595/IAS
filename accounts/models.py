from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class LoginInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genre= models.CharField(max_length=200,blank=True)
    
    def __str__(self) -> str:
        return str(self.user)