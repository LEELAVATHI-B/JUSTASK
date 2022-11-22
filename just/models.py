from django.db import models

# Create your models here.

class registration(models.Model):
    fullname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    phone_number=models.IntegerField()
    Date_of_birth=models.DateField()
    location=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.username