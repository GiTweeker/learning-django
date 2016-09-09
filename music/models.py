from django.db import models
from django.core.urlresolvers import reverse
from django.views.generic import CreateView


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})


    def __str__(self):

        return 'The album name is : ' +  self.album_title + ' The artist name is : ' + self.artist + '\n'





class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return 'The title of the song is : ' + self.song_title
