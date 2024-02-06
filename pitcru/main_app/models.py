
import requests
from django.db import models
from django.urls import reverse

API_KEY = "sDR8LF/Y92EM5TcNfaQxVg==vKgPW0X07hL86rUt"

# Create your models here.
class Car(models.Model):
  city_mpg = models.IntegerField()
  car_class = models.CharField(max_length=100)
  combination_mpg=models.IntegerField()
  cylinders = models.IntegerField()
  displacement = models.FloatField()
  drive = models.CharField(max_length=10)
  fuel_type = models.CharField(max_length = 10)
  gas = models.CharField(max_length=20)
  highway_mpg = models.IntegerField()
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  transmission = models.CharField(max_length=20)
  year = models.IntegerField()

  def __str__(self):
    return f"{self.year} {self.make} {self.model} ({self.id})"
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'car_id': self.id})

class Comment(models.Model):
  name = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  content = models.TextField(max_length = 500)
  date = models.DateField('feeding date')
  car = models.ForeignKey(
      Car,
      on_delete=models.CASCADE
  )
  
  def __str__(self):
      return f"{self.name} commented on {self.date}"

  class Meta:
      ordering = ['-date']

def seed_db():
  year = '2000'
  model = 'camry'
  api_url = f'https://api.api-ninjas.com/v1/cars?model={model}&year={year}'
  response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
  data = eval(response.text)
  for index_car in data:
    instance = Car(city_mpg=-index_car['city_mpg'], car_class = index_car['class'] , combination_mpg = index_car['combination_mpg'] , cylinders = index_car['cylinders'] , displacement = index_car['displacement'] , drive = index_car['drive'] , fuel_type=index_car['fuel_type'], highway_mpg = index_car['highway_mpg']  , make = index_car['make'],model=index_car['model'],transmission = index_car['transmission'],year=index_car['year'] )
    print(instance)
    instance.save()
