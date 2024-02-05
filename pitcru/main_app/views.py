# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def cars(request):
  return render(request, 'cars/index.html')


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
							                          