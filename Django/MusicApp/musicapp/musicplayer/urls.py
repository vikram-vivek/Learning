from django.conf.urls import url
from musicplayer import views

app_name = "musicplayer"

urlpatterns = [
    url(r'^$',views.TrackListView.as_view(),name='track_list'),
    url(r'^track/(?P<pk>\d+)$',views.TrackDetailView.as_view(),name='track_detail'),
    url(r'^track/new/$',views.CreateTrackView.as_view(),name='track_new'),
    url(r'^track/(?P<pk>\d+)/edit/$',views.UpdateTrackView.as_view(),name='track_edit'),
    url(r'^track/(?P<pk>\d+)/remove/$',views.DeleteTrackView.as_view(),name='track_remove'),
    url(r'new/event/$',views.CreateEventView.as_view(),name='create_event'),
    url(r'createevent/$',views.createevent,name='createevent'),
    url(r'^event/(?P<pk>\d+)$',views.EventDetailView.as_view(),name='event_detail'),
]
