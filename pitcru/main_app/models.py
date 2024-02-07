
import requests
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


car_list = [
"Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "Volkswagen", "Dodge", "Pontiac", "Oldsmobile", "Buick", "Plymouth", "Chrysler", "Mercedes-Benz", "BMW", "Mazda", "GMC", "Jeep", "Subaru", "Volvo", "Mitsubishi", "Mercury", "Cadillac", "Isuzu", "Lincoln", "Saab", "Jaguar", "Lexus", "Acura", "Alfa Romeo", "Audi", "Fiat", "Land Rover", "Porsche", "Suzuki", "Hyundai", "Kia", "Daihatsu", "Peugeot", "Renault", "Opel", "Lancia", "Citroën", "Triumph", "Datsun", "Infiniti", "Pontiac", "AMC", "Geo", "Plymouth", "Eagle"]

year_list = [
"1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
API_KEY = "sDR8LF/Y92EM5TcNfaQxVg==vKgPW0X07hL86rUt"


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  avatar = models.ImageField(default='default.jpg',upload_to='profile_images')
  bio = models.TextField
  
# Create your models here.
class Car(models.Model):
  city_mpg = models.IntegerField()
  car_class = models.CharField(max_length=100)
  combination_mpg=models.IntegerField()
  cylinders = models.IntegerField()
  displacement = models.FloatField()
  drive = models.CharField(max_length=10)
  fuel_type = models.CharField(max_length = 10)
  highway_mpg = models.IntegerField()
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  transmission = models.CharField(max_length=20)
  year = models.IntegerField()
  user = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.year} {self.make} {self.model} ({self.id})"
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'car_id': self.id})

class Comment(models.Model):
  name = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  content = models.TextField(max_length = 500)
  date_created= models.DateField()
  last_updated= models.DateField()
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  car = models.ForeignKey(
      Car,
      on_delete=models.CASCADE
  )
  
  def __str__(self):
      return f"{self.name} commented on '{self.date_created}'"

  class Meta:
      ordering = ['-date_created']

def seed_db():
  for carmake in car_list:
    make= carmake
    print(make)
    # for caryear in year_list:    
    year = '1985'
      # print(year)
    api_url = f'https://api.api-ninjas.com/v1/cars?limit=1&make={make}&year={year}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    data = eval(response.text)
    if len(data) > 0:
      print(data)
      for index_car in data:
        instance = Car(city_mpg=-index_car['city_mpg'], car_class = index_car['class'] , combination_mpg = index_car['combination_mpg'] , cylinders = index_car['cylinders'] , displacement = index_car['displacement'] , drive = index_car['drive'] , fuel_type=index_car['fuel_type'], highway_mpg = index_car['highway_mpg']  , make = index_car['make'],model=index_car['model'],transmission = index_car['transmission'],year=index_car['year'] )
        print(instance)
        instance.save()

  car_instances = [car for car in Car.objects.all()[:6]]
  
  # Instance 1
  comment1 = Comment(
    name='Jud',
    title="Ol' reliable",
    content='Best car ever',
    date='2024-02-05',
    car=car_instances[0]
  )

  # Instance 2
  comment2 = Comment(
    name='Alice',
    title='Impressive Performance',
    content='I love the speed and handling!',
    date='2024-02-06',
    car=car_instances[1]
  )

  # Instance 3
  comment3 = Comment(
    name='Bob',
    title='Fuel Efficiency',
    content='Great on gas mileage!',
    date='2024-02-07',
    car=car_instances[1]
  )

  # Instance 4
  comment4 = Comment(
    name='Eva',
    title='Sleek Design',
    content='The exterior design is stunning.',
    date='2024-02-08',
    car=car_instances[3]
  )

  # Instance 5
  comment5 = Comment(
    name='Alex',
    title='Comfortable Ride',
    content='Very comfortable for long drives.',
    date='2024-02-09',
    car=car_instances[3]
  )

  # Instance 6
  comment6 = Comment(
    name='Chris',
    title='Tech Features',
    content='Love the advanced technology features!',
    date='2024-02-10',
    car=car_instances[4]
  )

  # Instance 7
  comment7 = Comment(
    name='Sophie',
    title='Reliable Companion',
    content='Never had any major issues. A reliable choice.',
    date='2024-02-11',
    car=car_instances[4]
  )

  # Instance 8
  comment8 = Comment(
    name='Michael',
    title='Spacious Interior',
    content='The interior space is impressive.',
    date='2024-02-12',
    car=car_instances[4]
  )

  # Instance 9
  comment9 = Comment(
    name='Lily',
    title='Family Friendly',
    content='Perfect for a family with plenty of space.',
    date='2024-02-13',
    car=car_instances[5]
  )

  # Instance 10
  comment10 = Comment(
    name='Tom',
    title='Safety First',
    content='Top-notch safety features make me feel secure.',
    date='2024-02-14',
    car=car_instances[5]
  )

  # Instance 11
  comment11 = Comment(
    name='Sara',
    title='Easy to Maintain',
    content='Low maintenance and cost-effective.',
    date='2024-02-15',
    car=car_instances[5]
  )

  # Instance 12
  comment12 = Comment(
    name='Ryan',
    title='Great Resale Value',
    content='Holds its value well over time.',
    date='2024-02-16',
    car=car_instances[5]
  )
  comment_list = [
    comment1,
    comment2,
    comment3,
    comment4,
    comment5,
    comment6,
    comment7,
    comment8,
    comment9,
    comment10,
    comment11,
    comment12
  ]

  for comment in comment_list:
    print(comment)
    comment.save()