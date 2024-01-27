from django.db import models

# Create your models here.
class officer(models.Model):
    officername=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.DateField()
    address=models.CharField(max_length=30)
    contactnum=models.IntegerField()
    uname=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    did=models.IntegerField(default=1)
    sid=models.IntegerField(default=1)
class assigncase(models.Model):
    cmpid=models.IntegerField()
    offid=models.IntegerField()
    status=models.CharField(max_length=20)
    cremarks=models.CharField(max_length=200,default='')
