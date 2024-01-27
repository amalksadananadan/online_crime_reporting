from django.db import models

# Create your models here.
class login(models.Model):
    uname=models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)
    utype=models.CharField(max_length=20)

class designation(models.Model):
    dname=models.CharField(max_length=20)

class district(models.Model):
    disname=models.CharField(max_length=20)

class circle(models.Model):
    circlename=models.CharField(max_length=20)
    disid=models.IntegerField()

class station(models.Model):
    sname=models.CharField(max_length=20)
    scode=models.IntegerField()
    enum=models.IntegerField()
    cnum=models.IntegerField()
    uname=models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)
    cid = models.IntegerField()



