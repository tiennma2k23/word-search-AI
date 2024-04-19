from django.shortcuts import render, redirect # redirect: chuyen huong user toi page khac
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from myproject.main import *


# Create your views here.
# gửi request tới thư mục templates để tìm file index.html
def index(request):
    # dictionary 
    return render(request, 'login.html')


# sign up function
def register(request):  
    # check if the page is rendered with a post method
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # check if email already exist in database
        if User.objects.filter(email = email).exists():
            messages.info(request, 'Email Already Used')
            return redirect('register')
        # check if username alread exist in database
        elif User.objects.filter(username = username).exists():
            messages.info(request, 'Username Already Used')
            return redirect('register')
        # info valid -> create user
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')
    else: 
        return render(request, 'register.html')
    
# log in function
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # xac minh user
        user = auth.authenticate(username=username, password=password)

        # check if user is register or not
        if user is not None:
            auth.login(request, user)
            return redirect('wordsearch')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login.html')
    else:
        return render(request, 'login.html')

# log out
def logout(request):
    auth.logout(request) # log all user out of platform
    return redirect('/')

def wordsearch(request):
    return render(request, 'wordsearch.html')

def generate(request):
    if request.method == 'POST':
        name = request.POST['name']
        lesson = request.POST['lesson']
        grade = request.POST['grade']
    createPuzzle(name, lesson, grade)
    return render(request, 'wordsearch.html')

