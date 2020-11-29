from django.urls import path
from .views import home, contacto, login, trabajos


urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('login/', login, name="login"),
    path('trabajos/', trabajos, name="trabajos"),
    
]