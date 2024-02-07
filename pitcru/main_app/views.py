from django.shortcuts import render, redirect
from .models import Car, Comment

# Create your views here.
def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    comments = Comment.objects.get_queryset().filter(car=car) #grabs only comments associated with the specified car
    return render(request, 'cars/detail.html', {
        'car': car,
        'comments': comments
    })
  
def about(request):
    return render(request, 'about.html')

def cars(request):
    index_cars = Car.objects.all()
    return render(request, 'cars/index.html',{
    'cars':index_cars
    })

def home(request):
  cars = Car.objects.get_queryset().filter(is_featured=True)
  return render(request, 'homepage.html', {'cars': cars})
