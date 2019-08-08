from django.db import models

# Create your models here.
class Track(models.Model):
    track_id = models.CharField(max_length=255,unique=True)
    track_location = models.CharField(max_length=255,unique=True)

    def get_absolute_url(self):
        return reverse("track_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.track_id

class Event(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    track_id = models.ForeignKey('musicplayer.Track',related_name='events',on_delete=models.CASCADE)
    track_start_time = models.DateTimeField(blank=True,null=True)
    track_end_time = models.DateTimeField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse("event_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.track_id
