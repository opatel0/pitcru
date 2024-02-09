from django.shortcuts import render, redirect
from .models import Car, Comment
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import CommentForm
from datetime import datetime
import requests
API_KEY = "sDR8LF/Y92EM5TcNfaQxVg==vKgPW0X07hL86rUt"

# Create your views here.
def cars_detail(request, car_id):
    try:
      car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
      raise Http404("Car does not exist")
    comment_form = CommentForm()
    comments = Comment.objects.get_queryset().filter(car=car)
    return render(request, 'cars/detail.html', {
        'car': car,
        'comments': comments,
        'comment_form': comment_form
    })
  
def about(request):
    return render(request, 'about.html')

def showsearch(request):
    return render(request, 'advanced_search.html')

def search(request):
    data=request.POST
    year = data['year']
    model = data['model']
    if year != '':
      yearstring = f'year={year}&'
    else:
       yearstring = ''
    if model != '':
      modelstring = f'model={model}&'
    else:
       modelstring = ''
    api_url = f'https://api.api-ninjas.com/v1/cars?limit=1&{yearstring}{modelstring}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    cardata = eval(response.text)
    print(cardata)
    return redirect('cars')  

def cars(request):
    index_cars = Car.objects.all()
    return render(request, 'cars/index.html',{
    'cars':index_cars
    })

def home(request):
  cars = Car.objects.get_queryset().filter(is_featured=True)
  return render(request, 'homepage.html', {'cars': cars})

def profile(request):
  comments = request.user.comment_set.all()
  cars = Car.objects.get_queryset().filter(is_featured=True)
  return render(request, 'registration/profile.html', {'cars': cars,'comments':comments})

def addcomment(request,car_id):
  if(request.method=="POST"):
    form = CommentForm(request.POST)
    if form.is_valid():
      new_comment = form.save(commit=False)
      new_comment.car_id = car_id
      new_comment.user = request.user
      new_comment.date_created = datetime.today()
      new_comment.last_updated = datetime.today()
      new_comment.save()
  return redirect('details', car_id=car_id)

def editcommentshow(request,comment_id):
  comment = request.user.comment_set.filter(id=comment_id).get()
  return render(request, 'edit/comments.html', {
      'comment': comment
  })

def editcomment(request,comment_id):
    data=request.POST
    print(data)
    request.user.comment_set.filter(id=comment_id).update(title=data['Title'],content=data['Content'],name=data['Name'],last_updated=datetime.today())
    return redirect('profile')

def deletecomment(request,comment_id):
  request.user.comment_set.filter(id=comment_id).delete()
  return redirect('profile')

@login_required
def logout_view(request): 
  logout(request)
  return redirect('/')


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():								                          
      user = form.save()
      login(request, user) 
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again' 
  form = UserCreationForm() 
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context) 

def search(request):
    data=request.POST
    year = data['year']
    make = data['make']
    model = data['model']
    if year != '':
      yearstring = f'year={year}&'
    else:
       yearstring = ''
    if make != '':
       makestring = f'make={make}&'
    else:
       makestring = ''
    if model != '':
      modelstring = f'model={model}&'
    else:
       modelstring = ''
    api_url = f'https://api.api-ninjas.com/v1/cars?limit=1&{yearstring}{makestring}{modelstring}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    cardata = eval(response.text)
    print(cardata)
    return redirect('cars')