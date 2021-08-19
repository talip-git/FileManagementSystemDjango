from django.db import models
import datetime

from django.db.models.base import Model
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

class Document(models.Model):
    document_name = models.CharField(max_length=30,default='undefined')
    version = models.IntegerField(default=1)
    change_date = models.DateTimeField(default=datetime.datetime.now())
    file = models.BinaryField()
    desc = models.TextField()
    status = models.CharField(max_length=50,default='Not Finished')
    field = models.CharField(max_length=20,default='Not defined')
