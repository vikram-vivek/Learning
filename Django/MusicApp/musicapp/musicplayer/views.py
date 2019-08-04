from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def explorer(request):
    path = 'E:\MusicFiles'
    file_list = os.listdir(path)
    return HttpResponse("List of files %s "%file_list)

def playsong(request):
    path = 'E:/Numb.mp3'
    return render(request,'base.html')

def login_page(request):
    form = LoginForm(request.POST or None)
    print("User is Logged In : %s"%request.user.is_authenticated)
    context = {
        'form':form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("User is Logged In : %s"%request.user.is_authenticated)
            login(request,user)
            context['form'] = LoginForm()
            return redirect("/login")
        else:
            print("Error")

    return render(request, "auth/login.html", context)

def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", {})
