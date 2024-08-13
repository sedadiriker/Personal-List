from django.db import models

# Create your models here.

class Personal(models.Model):
    id = models.AutoField(primary_key=True) 
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    email = models.EmailField()
    position = models.CharField(max_length = 50)

def __str__(self):
    return f"{self.firstname} {self.lastname}"
