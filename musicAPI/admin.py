from django.contrib import admin
from .models import Singer, Song, Album, Content

# Register your models here.
admin.site.register(Singer)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Content)
