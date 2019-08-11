from django.conf.urls import url
from musicplayer import views

urlpatterns = [
    url(r'^$',views.TrackListView.as_view(),name='track_list'),
    url(r'^track/(?P<pk>\d+)$',views.TrackDetailView.as_view(),name='track_detail'),
    url(r'^track/new/$',views.CreateTrackView.as_view(),name='track_new'),
    url(r'^track/(?P<pk>\d+)/edit/$',views.UpdateTrackView.as_view(),name='track_edit'),
    url(r'^track/(?P<pk>\d+)/remove/$',views.DeleteTrackView.as_view(),name='track_remove'),
]