from django.db import models

# Create your models here.
class profile(models.Model):
    name =models.CharField(max_length=100)
    email=models.EmailField()
    career=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    password=models.CharField(max_length=20)


