from django.shortcuts import render, redirect # redirect: chuyen huong user toi page khac
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Feature
from myproject.main import *


# Create your views here.
# gửi request tới thư mục templates để tìm file index.html
def index(request):
    # dictionary 
    return render(request, 'login.html')


# log in and sign up function
def register(request):  
    # check if the page is rendered with a post method
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:   
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
            messages.info(request, 'Password is not the same')
            return redirect('register')
    else: 
        return render(request, 'register.html')
    

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
            return redirect(request, 'login.html')
    else:
        return render(request, 'login.html')

# log out
def logout(request):
    auth.logout(request) # log all user out of platform
    return redirect('/')

# dynamic url
def post(request, pk):
    return render(request, 'post.html',{'pk':pk})

def wordsearch(request):
    return render(request, 'wordsearch.html')

def generate(request):
    if request.method == 'POST':
        name = request.POST['name']
        lesson = request.POST['lesson']
        grade = request.POST['grade']

    convert_2_pdf(name, lesson, grade)
    return render(request, 'wordsearch.html')
    