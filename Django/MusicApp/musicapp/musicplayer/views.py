from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import os
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,get_user_model
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Event,Track
from next_prev import next_in_order, prev_in_order
from .forms import EventForm, TrackForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    context = {
        'music_url':"https://doc-00-1o-docs.googleusercontent.com/docs/securesc/m7imn1c8aqfhf7gdcn8l3h8q9urnp1un/hv86gadpj7allpg60v3b33at70otg8u3/1565287200000/13759712319618516183/13759712319618516183/1iETMqDfT2c7zwzIDJdo2_DW5o95k85Ke?e=download"
    }
    return render(request,'test_base.html',context)
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

class TrackListView(generic.ListView):
    model = Track
    first = Track.objects.first()
    second = next_in_order(first)
    prev_in_order(second) == first # True
    last = prev_in_order(first, loop=True)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['next_song'] = self.second
        context['previous_song'] = self.last
        return context

class TrackDetailView(generic.DetailView):
    model = Track
    # default ordering
    #first = Track.objects.first()
    #second = next_in_order(first)
    #prev_in_order(second) == first # True
    #last = prev_in_order(first, loop=True)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        qs = Track.objects.all().order_by('id')
        current_song = self.get_object()
        previous_song = prev_in_order(current_song,qs=qs,loop=True)
        next_song = next_in_order(current_song,qs=qs,loop=True)
        context['next_song'] = next_song
        context['previous_song'] = previous_song
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

class CreateTrackView(LoginRequiredMixin,generic.CreateView):
    login_url = '/login/'
    redirect_field_name = 'musicplayer/track_detail.html'
    form_class = TrackForm
    model = Track

class UpdateTrackView(LoginRequiredMixin,generic.UpdateView):
    login_url = '/login/'
    redirect_field_name = 'musicplayer/track_detail.html'
    form_class = TrackForm
    model = Track

class DeleteTrackView(LoginRequiredMixin,generic.DeleteView):
    model = Track
    success_url = reverse_lazy('track_list')
####

class EventListView(generic.ListView):
    model = Event

class EventDetailView(generic.DetailView):
    model = Event

class CreateEventView(LoginRequiredMixin,generic.CreateView):
    login_url = '/login/'
    redirect_field_name = '/login/'
    form_class = EventForm
    model = Event


def createevent(request):
        print("Inside create event function")
        print(request)
        print(request.POST.get('user_id'))
        # return HttpResponseRedirect(request.path_info)
        data={}
        print(request.POST.get('track'))
        if request.method == 'POST':
            event=Event()
            # track=Track()
            event.user_id= request.user#request.POST.get('user_id')
            # event.track_id= request.POST.get('track')
            event.track_id= Track.objects.get(track_id=request.POST.get('track'))
            event.track_start_time= request.POST.get('track_start_time')
            event.track_end_time= request.POST.get('track_end_time')
            event.save()
            print("Event created")
            data['message'] = 'Event added.'
            # return HttpResponseRedirect(request.path_info)
        else:
            data['message'] = 'Event was not added.'
            # return HttpResponseRedirect(request.path_info)

        return JsonResponse(data)



class EventDetailView(generic.DetailView):
    model = Event
