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

def home(request):
  cars = Car.objects.all()
  return render(request, 'homepage.html', {'cars': cars})