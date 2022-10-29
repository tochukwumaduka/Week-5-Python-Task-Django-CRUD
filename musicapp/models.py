from datetime import datetime
from email.policy import default
from operator import truediv
from unittest.util import _MAX_LENGTH
from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
# Attributes for “Artiste” : first_name, last_name, age
    first_name = models.CharField(max_length = 400, blank=True)
    last_name = models.CharField(max_length = 400, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__ (self):
        return self.first_name 



class Song(models.Model):
# Attributes for “Song” : title, date released, likes, artiste_id    
    title = models.CharField(max_length = 400, blank=True)
    date_released = models.DateTimeField(default=datetime.now, blank=True)

    likes = models.IntegerField(default=1)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE, default=1)


class Lyric(models.Model):
# Attributes for “Lyric”: content, song_id
    content = models.CharField(max_length = 400, blank=True)
    song_id = models.ForeignKey(Song,  on_delete=models.CASCADE, default=1)