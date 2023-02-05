from django.db import models

# Create your models here.


class Singer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.singer}, {self.year})"


class Content(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    track_number = models.IntegerField()

    def __str__(self):
        return f"{self.album}, {self.song}, track # {self.track_number}"
