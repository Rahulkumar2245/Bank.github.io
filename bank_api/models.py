from django.db import models

# Create your models here.

class Bank(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Branch(models.Model):
    branch=models.CharField(max_length=100)
    ifsc=models.CharField(max_length=11)

    Bank=models.ForeignKey(Bank,on_delete=models.CASCADE)    
