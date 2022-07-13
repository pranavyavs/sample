from django.db import models

# Create your models here.
class register_tb(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class image_tb(models.Model):
    name=models.CharField(max_length=20)
    file=models.FileField()
    
class country_tb(models.Model):
    country=models.CharField(max_length=20)
class state_tb(models.Model):
    countryid=models.ForeignKey(country_tb,on_delete=models.CASCADE)
    state=models.CharField(max_length=20)
class place_tb(models.Model):
    countryid=models.ForeignKey(country_tb,on_delete=models.CASCADE)
    stateid=models.ForeignKey(state_tb,on_delete=models.CASCADE)
    place=models.CharField(max_length=20)
