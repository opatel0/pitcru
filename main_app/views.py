from django.shortcuts import render, redirect
from .models import Car, Comment
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.http import Http404
from .forms import CommentForm
from datetime import datetime
import requests
from bs4 import BeautifulSoup  
API_KEY = "sDR8LF/Y92EM5TcNfaQxVg==vKgPW0X07hL86rUt"

class CarListView(ListView):
  paginate_by = 12
  model = Car

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
    Car.objects.filter(is_searched=True).update(is_searched=False)
    try:
      api_url = f'https://api.api-ninjas.com/v1/cars?limit=50&{api_string}'
      response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
      api_result = eval(response.text)
      for index_car in api_result:
        data_compare=Car.objects.get_queryset().filter(city_mpg=index_car['city_mpg'], car_class = index_car['class'] , combination_mpg = index_car['combination_mpg'] , cylinders = index_car['cylinders'] , displacement = index_car['displacement'] , drive = index_car['drive'] , fuel_type=index_car['fuel_type'], highway_mpg = index_car['highway_mpg']  , make = index_car['make'],model=index_car['model'],transmission = index_car['transmission'],year=index_car['year'])
        if(bool(data_compare)==False):
          search_string=f'{index_car["model"]}+{index_car["year"]}+vehicle'
          index_car['car_image']=findimage(search_string)
          instance = Car(car_image=index_car['car_image'], city_mpg=index_car['city_mpg'], car_class = index_car['class'] , combination_mpg = index_car['combination_mpg'] , cylinders = index_car['cylinders'] , displacement = index_car['displacement'] , drive = index_car['drive'] , fuel_type=index_car['fuel_type'], highway_mpg = index_car['highway_mpg']  , make = index_car['make'],model=index_car['model'],transmission = index_car['transmission'],year=index_car['year'],is_featured=False,is_searched=True,user_id = 1)
          instance.save()
        else:
          if(len(data_compare[0].car_image)==0):
            search_string=f'{index_car["model"]}+{index_car["year"]}+vehicle'
            index_car['car_image']=findimage(search_string)
            Car.objects.filter(id=data_compare[0].id).update(car_image = index_car['car_image'],is_searched=True)
          else:   
            Car.objects.filter(id=data_compare[0].id).update(is_searched=True)          
      showcar= Car.objects.get_queryset().filter(is_searched=True)
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


def getdata(url):  
    r = requests.get(url)  
    return r.text  
def findimage(data):
    htmldata = getdata(f"https://www.google.com/search?sca_esv=11b4f3157143913f&sxsrf=ACQVn0-1wFCM3bFrwEMwrb7h_z2St3_QNA:1707457507118&q={data}&tbm=isch&source=lnms&prmd=ivsnmbtz&sa=X&ved=2ahUKEwiv3bjxxp2EAxUVkmoFHZuXAC4Q0pQJegQIHhAB&cshid=1707457509902846&biw=1872&bih=958&dpr=1") 
    soup = BeautifulSoup(htmldata, 'html.parser') 
    count = 0 
    for item in soup.find_all('img'): 
      image = item['src']
      count += 1
      if count == 2:
        break
    return(image)
