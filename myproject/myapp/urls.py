from django.urls import path
from . import views
import sys

print(sys.executable)
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('wordsearch', views.wordsearch, name='wordsearch'),
    path('generate', views.generate, name="generate"),
    # path()
    path('guide', views.guide,name="guide" ),
    path('about_us',views.about_us, name="about_us"),
    path('home',views.home, name="home")
] 
