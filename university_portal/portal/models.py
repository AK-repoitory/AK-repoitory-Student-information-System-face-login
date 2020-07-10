from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    croll = models.IntegerField(default=0)
    cname = models.CharField(max_length=20, default="")
    cemail = models.EmailField(max_length=20, default="")
    query = models.TextField()

    def __str__(self):
        return 'Message from '+ self.cname


class Marks(models.Model):
    username = models.CharField(max_length=15,default="")
    first_name =models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    rollno = models.IntegerField(default=0)
    Subject_c = models.FloatField(default=0)
    Subject_Networking = models.FloatField(default=0)
    Subject_java = models.FloatField(default=0)
    Subject_c = models.FloatField(default=0)
    Subject_python = models.FloatField(default=0)
    email = models.EmailField(max_length=20, default="")
    birthday = models.DateField(default=datetime.now)

    def __str__(self):
        return 'Marks from '+ self.username
