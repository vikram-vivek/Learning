from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'test_base.html')
    #return HttpResponse("Hello World!")

def explorer(request):
    path = 'static\\musicapp\\audiofiles'
    file_list = os.listdir(path)
    return HttpResponse("List of files %s "%file_list)

def playsong(request):
    path = 'static\\musicapp\\audiofiles'
    song_list = os.listdir(path)
    context = {
        'song_list':song_list
    }
    return render(request,'base.html',context)

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
            return redirect("/playsong")
        else:
            print("Error")

    return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username,email,password)
        print(new_user)
        return redirect("/login")
    return render(request, "auth/register.html", context)
