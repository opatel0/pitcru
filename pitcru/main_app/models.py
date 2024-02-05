from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
  
class Car(models.Model):
  city_mpg = models.IntegerField()
  car_class = models.CharField(max_length=50)
  combination_mpg = models.IntegerField()
  cylinders = models.IntegerField()
  displacement = models.FloatField()
  drive = models.CharField(max_length=4)
  fuel_type = models.CharField(max_length = 15)
  highway_mpg = models.IntegerField()
  make = models.CharField(max_length = 100)
  model = models.CharField(max_length = 100)
  transmission = models.CharField(max_length = 20)
  year = models.IntegerField()
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  
  # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
  def __str__(self):
    return f'{self.model} ({self.id})'