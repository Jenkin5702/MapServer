# models.py
from django.db import models
 
class Test(models.Model):
    name=models.CharField(max_length=20)

class Communicate(models.Model):
    userName=models.CharField(max_length=20)
    ctime=models.CharField(max_length=20)
    Location=models.CharField(max_length=124)
    imageUrl=models.CharField(max_length=300)
    content=models.CharField(max_length=300)
    zan=models.CharField(max_length=4)

class Location(models.Model):
    name=models.CharField(max_length=30)
    people=models.CharField(max_length=3)

class UserInfo(models.Model): 
    userName= models.CharField(max_length=20)
    pasword= models.CharField(max_length=20)
    iden= models.CharField(max_length=20)
    realName= models.CharField(max_length=20)

class Delegate(models.Model): 
    userName= models.CharField(max_length=20)
    dtime= models.CharField(max_length=20)
    location=models.CharField(max_length=24)
    locationLat=models.CharField(max_length=12)
    locationLng=models.CharField(max_length=12)
    remark= models.CharField(max_length=300)

class Notif(models.Model): 
    portraitRes= models.CharField(max_length=200)
    pubTime= models.CharField(max_length=40)
    content= models.CharField(max_length=300)
    username= models.CharField(max_length=20)
    locationLat =models.CharField(max_length=12)
    locationLng =models.CharField(max_length=12)