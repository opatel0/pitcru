from django.urls import path
from .import views
from django.contrib.auth import logout

urlpatterns = [
  path('', views.home, name='home'),
  path('cars/', views.cars, name='cars'),
]