from django.db import models

# Create your models here.

class Employee(models.Model):
    empno = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=20)
    empsalary = models.FloatField(null=False,blank=False)
    
    
    

        
    