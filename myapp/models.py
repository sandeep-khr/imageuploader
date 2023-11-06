from django.db import models

# Create your models here.
    
class Catetgory(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Image(models.Model):
    photo = models.ImageField(upload_to='myimage')
    date = models.DateField(auto_now_add=True)
    # cat = models.ForeignKey('Category', on_delete=models.SET_NULL)