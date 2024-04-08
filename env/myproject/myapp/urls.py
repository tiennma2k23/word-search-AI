from django.urls import path
from . import views
import sys

print(sys.executable)
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('wordsearch', views.wordsearch, name='wordsearch'),
    path('generate', views.generate, name="generate")
] 
