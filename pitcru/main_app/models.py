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
    car_list = [car1, car2, car3, car4, car5, car6]

    for car in car_list:
        print(car)
        car.save()
        # comment = Comment(
    #     name = 'Jud',
    #     title = "Ol' reliable",
    #     content = 'Best car ever',
    #     date = '2024-02-05',
    #     car = 
    # )

    
    