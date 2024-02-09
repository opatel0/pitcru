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
    api_string = make_search_string(data)
    try:
      api_url = f'https://api.api-ninjas.com/v1/cars?limit=1&{api_string}'
      response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
      index_car = eval(response.text)
      print(index_car)
      data_compare=Car.objects.get_queryset().filter(model=index_car[0]["model"])
      if(bool(data_compare)==False):
        instance = Car(city_mpg=index_car[0]['city_mpg'], car_class = index_car[0]['class'] , combination_mpg = index_car[0]['combination_mpg'] , cylinders = index_car[0]['cylinders'] , displacement = index_car[0]['displacement'] , drive = index_car[0]['drive'] , fuel_type=index_car[0]['fuel_type'], highway_mpg = index_car[0]['highway_mpg']  , make = index_car[0]['make'],model=index_car[0]['model'],transmission = index_car[0]['transmission'],year=index_car[0]['year'],is_featured=False,user_id = 1)
        instance.save()
      showcar=Car.objects.get_queryset().filter(model=index_car[0]["model"])
      return render(request, 'cars/index.html',{
      'cars':showcar
      })
    except:
      return redirect('/')

def make_search_string(postdata):
    year = postdata['year']
    make = postdata['make']
    model = postdata['model']
    min_combo_mpg = postdata['min_combo_mpg']
    min_city_mpg = postdata['min_city_mpg']
    min_hwy_mpg = postdata['min_hwy_mpg']
    cylinders = postdata['cylinder']
    transmission = postdata['transmission']
    fuel_type = postdata['fuel_type']
    drive = postdata['drive']
    if year != '':
      year_string = f'year={year}&'
    else:
      year_string = ''
    if model != '':
      model_string = f'model={model}&'
    else:
      model_string = ''
    if make != '':
      make_string = f'model={make}&'
    else:
      make_string = ''
    if min_combo_mpg != '':
      min_combo_mpg_string = f'min_combo_mpg={min_combo_mpg}&'
    else:
      min_combo_mpg_string = ''
    if min_city_mpg != '':
      min_city_mpg_string = f'min_city_mpg={min_city_mpg}&'
    else:
      min_city_mpg_string = ''
    if min_hwy_mpg != '':
      min_hwy_mpg_string = f'min_hwy_mpg={min_hwy_mpg}&'
    else:
      min_hwy_mpg_string = ''
    if cylinders != '':
      cylinders_string = f'cylinders={cylinders}&'
    else:
      cylinders_string = ''
    if transmission != '':
      transmission_string = f'transmission={transmission}&'
    else:
      transmission_string = ''
    if fuel_type != '':
      fuel_type_string= f'fuel_type={fuel_type}&'
    else:
      fuel_type_string = ''
    if drive != '':
      drive_string = f'drive={drive}&'
    else:
      drive_string = ''
      
    return_string = f'{year_string}{make_string}{model_string}{min_combo_mpg_string}{min_city_mpg_string}{min_hwy_mpg_string}{cylinders_string}{transmission_string}{fuel_type_string}{drive_string}'
    return return_string

def cars(request):
  index_cars = Car.objects.all()
  return render(request, 'cars/index.html',{
  'cars':index_cars
  })

def home(request):
  cars = Car.objects.get_queryset().filter(is_featured=True)
  return render(request, 'homepage.html', {'cars': cars})

def profile(request):
  cars = request.user.car_set.all()
  comments = request.user.comment_set.all()
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
