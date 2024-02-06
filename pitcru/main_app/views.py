from django.shortcuts import render, redirect
from .models import Car, Comment
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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
  cars = Car.objects.all()
  return render(request, 'homepage.html', {'cars': cars})


@login_required
def logout_view(request):
  logout(request)
  return render(request, 'home.html')


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():								                          
      user = form.save()
      login(request, user) 
      return redirect('/home/')
    else:
      error_message = 'Invalid sign up - try again' 
  form = UserCreationForm() 
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context) 