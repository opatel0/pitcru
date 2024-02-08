from django.shortcuts import render, redirect
from .models import Car, Comment
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from datetime import datetime


# Create your views here.
def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    comment_form = CommentForm()
    comments = Comment.objects.get_queryset().filter(car=car) #grabs only comments associated with the specified car
    return render(request, 'cars/detail.html', {
        'car': car,
        'comments': comments,
        'comment_form': comment_form
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