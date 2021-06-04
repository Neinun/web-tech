from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, '../templates/core/base.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password2==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return render(request, '../templates/core/signup.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return render(request, '../templates/core/signup.html')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, password=password1, email=email)
                user.save()
                messages.info(request,'Log in to continue')
                return render(request, '../templates/core/base.html')
        else:
            messages.info(request, 'Passwords doesnt match')
            return render(request, '../templates/core/signup.html')
    else:
        return render(request, '../templates/core/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request, 'Sucessfully logged in')
            # Here instead of base.html feed has to be rendered
            return render(request, '../templates/core/base.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request, '../templates/core/login.html')
    else:
        return render(request, '../templates/core/login.html')