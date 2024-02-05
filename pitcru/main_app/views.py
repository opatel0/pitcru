from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    redirect('about/')

def about(request):
    return render(request, 'about.html')