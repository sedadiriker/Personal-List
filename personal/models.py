from django.db import models

# Create your models here.

class Personal(models.Model):
    id = models.AutoField(primary_key=True) 
    firstname = models.CharField(max_length = 100, verbose_name = 'firstname',)
    lastname = models.CharField(max_length = 100)
    email = models.EmailField()
    position = models.CharField(max_length = 50)
    
    class Meta:
        verbose_name = 'personal list'
