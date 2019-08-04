from django.shortcuts import render
from django.http import HttpResponse
import os
from .forms import LoginForm

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
    return render(request, "auth/login.html", context)

def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", {})
