from django.shortcuts import render

# Create your views here.
def cars_detail(request, car_id):
    return render(request, 'cars/detail.html')