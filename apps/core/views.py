from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, '../templates/core/base.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = UserCreationForm()
        return render(request, '../templates/core/signup.html', {'form': form})

def login(request):
    return render(request, '../templates/core/login.html')