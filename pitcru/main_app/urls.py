from django.urls import path
from .import views
from django.contrib.auth import logout

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cars/', views.cars, name='cars'),
  path('accounts/logout/', views.logout_view),
  path('accounts/signup/', views.signup, name='signup')
]
