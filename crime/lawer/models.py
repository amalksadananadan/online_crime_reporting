from django.db import models

# Create your models here.
class lawyerreg(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    hname=models.CharField(max_length=20)
    street=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    pin=models.IntegerField()
    country=models.CharField(max_length=20)
    photo=models.FileField(upload_to="file")
    qual=models.FileField(upload_to="file")
    proof=models.FileField(upload_to="file")
    uname=models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)
    status=models.CharField(max_length=20, default='')