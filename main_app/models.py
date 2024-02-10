import requests
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import requests
from bs4 import BeautifulSoup  
from django.contrib.postgres.fields import ArrayField  
from django.db.models.signals import post_save
from django.dispatch import receiver

car_list = [
"Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "Volkswagen", "Dodge", "Pontiac", "Oldsmobile", "Buick", "Plymouth", "Chrysler", "Mercedes-Benz", "BMW", "Mazda", "GMC", "Jeep", "Subaru", "Volvo", "Mitsubishi", "Mercury", "Cadillac", "Isuzu", "Lincoln", "Saab", "Jaguar", "Lexus", "Acura", "Alfa Romeo", "Audi", "Fiat", "Land Rover", "Porsche", "Suzuki", "Hyundai", "Kia", "Daihatsu", "Peugeot", "Renault", "Opel", "Lancia", "Citroën", "Triumph", "Datsun", "Infiniti", "Pontiac", "AMC", "Geo", "Plymouth", "Eagle"]

year_list = [
"1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
API_KEY = "byXNgBjF0W/zXArLsaN4NA==Xvxio9Kva6c75BFT"
  
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  favorite_cars = ArrayField(models.IntegerField(null=True),null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
      Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Create your models here.
class Car(models.Model):
  car_image = models.CharField(max_length = 500)
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
  is_featured = models.BooleanField(default=False)
  is_searched = models.BooleanField(default=False)
  is_favorite = models.BooleanField(default=False)
  user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)

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
  user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
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
    make = carmake
    for caryear in year_list:    
      year = caryear
      api_url = f'https://api.api-ninjas.com/v1/cars?limit=1&make={make}&year={year}'
      response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
      data = eval(response.text)
      if len(data) > 0:
        for index_car in data:
          search_string=f'{index_car["model"]}+{index_car["year"]}+vehicle'
          seed_image=findimage(search_string)
          try:
            instance = Car(car_image=seed_image,city_mpg=index_car['city_mpg'], car_class = index_car['class'] , combination_mpg = index_car['combination_mpg'] , cylinders = index_car['cylinders'] , displacement = index_car['displacement'] , drive = index_car['drive'] , fuel_type=index_car['fuel_type'], highway_mpg = index_car['highway_mpg']  , make = index_car['make'],model=index_car['model'],transmission = index_car['transmission'],year=index_car['year'],is_searched=False,is_featured=False )
            instance.save()
            print(instance)
          except:
            pass

  car_instances = [car for car in Car.objects.all()[:6]]
  
  # Instance 1
  comment1 = Comment(
    name='Jud',
    title="Ol' reliable",
    content='Best car ever',
    date_created='2024-02-05',
    last_updated='2024-02-05',
    car=car_instances[0]
  )

  # Instance 2
  comment2 = Comment(
    name='Alice',
    title='Impressive Performance',
    content='I love the speed and handling!',
    date_created='2024-02-06',
    last_updated='2024-02-06',
    car=car_instances[1]
  )

  # Instance 3
  comment3 = Comment(
    name='Bob',
    title='Fuel Efficiency',
    content='Great on gas mileage!',
    date_created='2024-02-07',
    last_updated='2024-02-07',
    car=car_instances[1]
  )

  # Instance 4
  comment4 = Comment(
    name='Eva',
    title='Sleek Design',
    content='The exterior design is stunning.',
    date_created='2024-02-08',
    last_updated='2024-02-08',
    car=car_instances[3]
  )

  # Instance 5
  comment5 = Comment(
    name='Alex',
    title='Comfortable Ride',
    content='Very comfortable for long drives.',
    date_created='2024-02-09',
    last_updated='2024-02-09',
    car=car_instances[3]
  )

  # Instance 6
  comment6 = Comment(
    name='Chris',
    title='Tech Features',
    content='Love the advanced technology features!',
    date_created='2024-02-10',
    last_updated='2024-02-10',
    car=car_instances[4]
  )

  # Instance 7
  comment7 = Comment(
    name='Sophie',
    title='Reliable Companion',
    content='Never had any major issues. A reliable choice.',
    date_created='2024-02-11',
    last_updated='2024-02-11',
    car=car_instances[4]
  )

  # Instance 8
  comment8 = Comment(
    name='Michael',
    title='Spacious Interior',
    content='The interior space is impressive.',
    date_created='2024-02-12',
    last_updated='2024-02-12',
    car=car_instances[4]
  )

  # Instance 9
  comment9 = Comment(
    name='Lily',
    title='Family Friendly',
    content='Perfect for a family with plenty of space.',
    date_created='2024-02-13',
    last_updated='2024-02-13',
    car=car_instances[5]
  )

  # Instance 10
  comment10 = Comment(
    name='Tom',
    title='Safety First',
    content='Top-notch safety features make me feel secure.',
    date_created='2024-02-14',
    last_updated='2024-02-14',
    car=car_instances[5]
  )

  # Instance 11
  comment11 = Comment(
    name='Sara',
    title='Easy to Maintain',
    content='Low maintenance and cost-effective.',
    date_created='2024-02-15',
    last_updated='2024-02-15',
    car=car_instances[5]
  )

  # Instance 12
  comment12 = Comment(
    name='Ryan',
    title='Great Resale Value',
    content='Holds its value well over time.',
    date_created='2024-02-16',
    last_updated='2024-02-16',
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
    comment.save()
    print(comment)
  
  print("SEEDING FEATURED CARS")
  years = ['2006', '2000', '2023', '1985', '1985', '1985', '2010', '1991', '2015', '2008', '2020', '1987']
  makes = ['subaru', 'toyota', 'maserati', 'alfa romeo', 'renault', 'dodge', 'ferrari', 'buick', 'ford', 'toyota', 'volkswagen', 'chevrolet']
  models = ['baja', 'celica', 'MC20', 'spider veloce 2000', 'fuego', 'charger', '458 italia', 'lesabre', 'mustang', 'yaris', 'tiguan', 'el camino']
  for year, make, model in zip(years, makes, models):
    api_url = f'https://api.api-ninjas.com/v1/cars?limit=1&year={year}&make={make}&model={model}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    data = eval(response.text)
    search_string=f'{data[0]["model"]}+{data[0]["year"]}+vehicle'
    featured_image=findimage(search_string)
    car = Car(
      car_image = featured_image,
      city_mpg = data[0]['city_mpg'],
      car_class = data[0]['class'],
      combination_mpg= data[0]['combination_mpg'],
      cylinders = data[0]['cylinders'],
      displacement = data[0]['displacement'],
      drive = data[0]['drive'],
      fuel_type = data[0]['fuel_type'],
      highway_mpg = data[0]['highway_mpg'],
      make = data[0]['make'],
      model = data[0]['model'],
      transmission = data[0]['transmission'],
      year = data[0]['year'],
      is_searched = False,
      is_featured = True
    )
    car.save()
    print(car)
  print("SEEDING PROCESS SUCCESSFUL")

def getdata(url):  
    r = requests.get(url)  
    return r.text  
def findimage(data):
    htmldata = getdata(f"https://www.google.com/search?sca_esv=11b4f3157143913f&sxsrf=ACQVn0-1wFCM3bFrwEMwrb7h_z2St3_QNA:1707457507118&q={data}&tbm=isch&source=lnms&prmd=ivsnmbtz&sa=X&ved=2ahUKEwiv3bjxxp2EAxUVkmoFHZuXAC4Q0pQJegQIHhAB&cshid=1707457509902846&biw=1872&bih=958&dpr=1")  
    soup = BeautifulSoup(htmldata, 'html.parser') 
    count = 0 
    seed_image = ''
    for item in soup.find_all('img'): 
      seed_image = item['src']
      count += 1
      if count == 2:
        break
    return(seed_image)