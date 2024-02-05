from django.shortcuts import render
from .models import Car

# Create your views here.
def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', {
        'car': car
    })