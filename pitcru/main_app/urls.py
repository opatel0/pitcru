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
    path('edit_comment/<int:comment_id>/', views.editcomment, name = 'edit_comment'),
    path('edit_show_comment/<int:comment_id>/',views.editcommentshow, name= 'edit_show_comment'),
    path('delete_comment/<int:comment_id>/', views.deletecomment, name = 'delete_comment'),
    path('search/', views.search, name = 'search'),
]




# import requests  
# from bs4 import BeautifulSoup  
    
# def getdata(url):  
#     r = requests.get(url)  
#     return r.text  
    
# htmldata = getdata("https://www.google.com/search?sca_esv=3c7692eee43ce5fe&sxsrf=ACQVn0-rx1SXJuF7BdDN4c3qsYt6CrFQSQ:1707447430762&q=silverado&tbm=isch&source=lnms&prmd=isvnmbtz&sa=X&ved=2ahUKEwjy79SsoZ2EAxVuke4BHVRmDNIQ0pQJegQIKhAB&biw=1872&bih=958&dpr=1")  
# soup = BeautifulSoup(htmldata, 'html.parser')  
# for item in soup.find_all('img'): 
#     print(item['src'])