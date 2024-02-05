from django.db import models
from django.urls import reverse

# Create your models here.
class Car(models.Model):
  year = models.CharField(max_length=4)
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  fuel_type = models.CharField(max_length=100)
  drive_transmission = models.CharField(max_length=100)
  cylinders = models.IntegerField()
  transmission = models.CharField(max_length=100)
  city_mileage_min = models.IntegerField()
  city_mileage_max = models.IntegerField()
  highway_mileage_min = models.IntegerField()
  highway_mileage_max = models.IntegerField()
  average_mileage_min = models.IntegerField()
  average_mileage_max = models.IntegerField()

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
  # Instance 1
  car1 = Car(
    year='2008',
    make='Toyota',
    model='Yaris',
    fuel_type='Regular',
    drive_transmission='Auto',
    cylinders=4,
    transmission='FWD',
    city_mileage_min=27,
    city_mileage_max=31,
    highway_mileage_min=33,
    highway_mileage_max=37,
    average_mileage_min=26,
    average_mileage_max=37
  )

  # Instance 2
  car2 = Car(
    year='2015',
    make='Honda',
    model='Civic',
    fuel_type='Regular',
    drive_transmission='Auto',
    cylinders=4,
    transmission='FWD',
    city_mileage_min=28,
    city_mileage_max=32,
    highway_mileage_min=36,
    highway_mileage_max=40,
    average_mileage_min=27,
    average_mileage_max=38
  )

  # Instance 3
  car3 = Car(
    year='2020',
    make='Ford',
    model='Focus',
    fuel_type='Regular',
    drive_transmission='Auto',
    cylinders=4,
    transmission='FWD',
    city_mileage_min=26,
    city_mileage_max=30,
    highway_mileage_min=34,
    highway_mileage_max=38,
    average_mileage_min=25,
    average_mileage_max=35
  )

  # Instance 4
  car4 = Car(
    year='2012',
    make='Chevrolet',
    model='Malibu',
    fuel_type='Regular',
    drive_transmission='Auto',
    cylinders=4,
    transmission='FWD',
    city_mileage_min=25,
    city_mileage_max=29,
    highway_mileage_min=33,
    highway_mileage_max=37,
    average_mileage_min=24,
    average_mileage_max=34
  )

  # Instance 5
  car5 = Car(
    year='2019',
    make='Nissan',
    model='Altima',
    fuel_type='Regular',
    drive_transmission='Auto',
    cylinders=4,
    transmission='FWD',
    city_mileage_min=27,
    city_mileage_max=31,
    highway_mileage_min=36,
    highway_mileage_max=40,
    average_mileage_min=26,
    average_mileage_max=37
  )

  # Instance 6
  car6 = Car(
    year='2016',
    make='Hyundai',
    model='Elantra',
    fuel_type='Regular',
    drive_transmission='Auto',
    cylinders=4,
    transmission='FWD',
    city_mileage_min=28,
    city_mileage_max=32,
    highway_mileage_min=37,
    highway_mileage_max=41,
    average_mileage_min=27,
    average_mileage_max=39
  )

  # Instance 1
  comment1 = Comment(
    name='Jud',
    title="Ol' reliable",
    content='Best car ever',
    date='2024-02-05',
    car=car1
  )

  # Instance 2
  comment2 = Comment(
    name='Alice',
    title='Impressive Performance',
    content='I love the speed and handling!',
    date='2024-02-06',
    car=car2
  )

  # Instance 3
  comment3 = Comment(
    name='Bob',
    title='Fuel Efficiency',
    content='Great on gas mileage!',
    date='2024-02-07',
    car=car2
  )

  # Instance 4
  comment4 = Comment(
    name='Eva',
    title='Sleek Design',
    content='The exterior design is stunning.',
    date='2024-02-08',
    car=car4
  )

  # Instance 5
  comment5 = Comment(
    name='Alex',
    title='Comfortable Ride',
    content='Very comfortable for long drives.',
    date='2024-02-09',
    car=car4
  )

  # Instance 6
  comment6 = Comment(
    name='Chris',
    title='Tech Features',
    content='Love the advanced technology features!',
    date='2024-02-10',
    car=car5
  )

  # Instance 7
  comment7 = Comment(
    name='Sophie',
    title='Reliable Companion',
    content='Never had any major issues. A reliable choice.',
    date='2024-02-11',
    car=car5
  )

  # Instance 8
  comment8 = Comment(
    name='Michael',
    title='Spacious Interior',
    content='The interior space is impressive.',
    date='2024-02-12',
    car=car5
  )

  # Instance 9
  comment9 = Comment(
    name='Lily',
    title='Family Friendly',
    content='Perfect for a family with plenty of space.',
    date='2024-02-13',
    car=car6
  )

  # Instance 10
  comment10 = Comment(
    name='Tom',
    title='Safety First',
    content='Top-notch safety features make me feel secure.',
    date='2024-02-14',
    car=car6
  )

  # Instance 11
  comment11 = Comment(
    name='Sara',
    title='Easy to Maintain',
    content='Low maintenance and cost-effective.',
    date='2024-02-15',
    car=car6
  )

  # Instance 12
  comment12 = Comment(
    name='Ryan',
    title='Great Resale Value',
    content='Holds its value well over time.',
    date='2024-02-16',
    car=car6
  )
  car_list = [car1, car2, car3, car4, car5, car6]
  comment_list = [comment1, comment2, comment3, comment4, comment5, comment6, comment7, comment8, comment9, comment10, comment11, comment12]
  for car in car_list:
    print(car)
    car.save()
  for comment in comment_list:
    print(comment)
    comment.save()
    