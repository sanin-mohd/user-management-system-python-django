from django.db import models

# Create your models here.
class profile(models.Model):
    name =models.CharField(max_length=100)
    email=models.EmailField()
    career=models.TextField()
    img=models.ImageField(upload_to='pics')

# a=profile()
# a.name='Kim Sarah'
# a.email='kim@gmail.com'
# a.career='Software Devoleper'
# a.img='https://i.imgur.com/sAtgYjl.jpg'
# b=profile()
# b.name='Sanin'
# b.email='sanin@gmail.com'
# b.career='Python Developer'
# b.img=''

