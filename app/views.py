from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def login(request):
    return render(request, 'app/login.html')

def trabajos(request):
    return render(request, 'app/trabajos.html')