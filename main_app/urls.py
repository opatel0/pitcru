from django.urls import path
from . import views

urlpatterns = [
    path('cars/<int:car_id>/', views.cars_detail, name='details'),
    path('cars/', views.cars, name='cars'),
    path('cars_index/', views.CarListView.as_view(), name='cars_index'),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('accounts/logout/', views.logout_view, name = 'logout'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile, name = 'profile'),
    path('comment/<int:car_id>/', views.addcomment, name = 'comment'),
    path('edit_comment/<int:comment_id>/', views.editcomment, name = 'edit_comment'),
    path('edit_show_comment/<int:comment_id>/',views.editcommentshow, name= 'edit_show_comment'),
    path('delete_comment/<int:comment_id>/', views.deletecomment, name = 'delete_comment'),
    path('search/', views.search, name = 'search'),
    path('add_car/<int:car_id>/', views.add_car, name = 'add_car'),
    path('delete_car/<int:car_id>/', views.delete_car, name = 'delete_car')
]
