from django.db import models

# Create your models here.


class Youtube(models.Model):
    title = models.CharField(max_length=30, unique=True)
    youtube_embed_url = models.CharField(max_length=200)
    youtube_video_url = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    time_to_start = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        url = self.youtube_video_url
        url = url[17:]
        return f"/chat/{url}/"


