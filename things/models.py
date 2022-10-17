from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(models.Model):
    name = models.CharField(blank = False, unique = True,max_length = 30)
    description = models.TextField(blank = True,unique = False,max_length = 120)
    quantity = models.IntegerField(unique = False,validators = [MinValueValidator(0),MaxValueValidator(100)])
# Create your models here.
