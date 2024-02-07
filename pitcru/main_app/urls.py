from django.urls import path
from . import views

urlpatterns = [
    path('cars/<int:car_id>/', views.cars_detail, name='details'),
    path('cars/', views.cars, name='cars'),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('accounts/logout/', views.logout_view, name = 'logout'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile, name = 'profile'),
    path('comment/<int:car_id>/', views.addcomment, name = 'comment'),
    path('commentedit/<int:comment_id>/', views.editcomment, name = 'editcomment'),
    path('commenteditshow/<int:comment_id>/',views.editcommentshow, name= 'editcommentshow'),
    path('commentdelete/<int:comment_id>/', views.deletecomment, name = 'deletecomment')
]
