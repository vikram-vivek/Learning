from django.shortcuts import render
from django.http import HttpResponse

def HomePage(request):
    return render(request,"home_page.html",{})

def AboutPage(request):
    return render(request,"home_page.html",{})

def ContactPage(request):
    context = {
        'title':'Contact Page'
    }
    return render(request,"contact/view.html",context)


def HomePage_old(request):
    return HttpResponse("<h1>Hello World!<h1>")
