from django.db import models

# Create your models here.
class complaint(models.Model):
    ctype=models.CharField(max_length=20)
    complaint=models.CharField(max_length=250)

    sid=models.IntegerField(default=1)
    ctid=models.IntegerField(default=1)
    status=models.CharField(max_length=20,default='')
class missing(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    age=models.IntegerField()
    height=models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    imarks=models.CharField(max_length=100)
    mdate=models.CharField(max_length=10)
    photo=models.FileField(upload_to="file")
    remarks=models.CharField(max_length=250)
    cid=models.IntegerField()
class theft(models.Model):
    date=models.CharField(max_length=20)
    object=models.CharField(max_length=20)
    model=models.CharField(max_length=20)
    quantity=models.CharField(max_length=20)
    identification=models.CharField(max_length=100)
    remarks=models.CharField(max_length=250)
    photo=models.FileField(upload_to="file")
    cid=models.IntegerField()

class criminal(models.Model):
    date=models.CharField(max_length=20)
    cname=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.CharField(max_length=50)
    contact=models.IntegerField()
    remarks=models.CharField(max_length=250)
    cid=models.IntegerField()
class citizenreg(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    hname=models.CharField(max_length=20)
    street=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    pin=models.IntegerField()
    country=models.CharField(max_length=20)
    uname=models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)
    status=models.CharField(max_length=20, default='')
class selectedlawer(models.Model):
    lid=models.IntegerField()
    cmpid=models.IntegerField()