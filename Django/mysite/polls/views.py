from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World! We are at the polls app")

def detail(request,question_id):
    return HttpResponse("You are looking at question %s" % question_id)

def results(reuest,question_id):
    return HttpResponse("You are looking at results of question %s" % question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on question %s" % question_id)