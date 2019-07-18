from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.http import Http404

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/details.html',{'question':question})

def results(reuest,question_id):
    return HttpResponse("You are looking at results of question %s" % question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on question %s" % question_id)