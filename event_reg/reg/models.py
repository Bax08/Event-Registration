from django.db import models


# Create your models here.

class Information(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=45)
    number = models.IntegerField()
   

    def __str__(self):
        return self.name 
       
class Details(models.Model):
    gender = models.CharField(max_length=10)
    state = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.gender, self.state}"
   
      


