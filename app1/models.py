from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class registermodel(User):
    phone=models.BigIntegerField()
    age=models.IntegerField()
    gender=models.CharField(max_length=5,choices=[['MALE','Male'],['FEMALE','Female']])
    dor=models.DateTimeField(default=timezone.now)