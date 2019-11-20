from django.forms import ModelForm
from .models import Youtube

# Create the form class.
class YoutubeModelForm(ModelForm):
    class Meta:
             model = Youtube
             fields = ['title', 'youtube_embed_url',
                       'youtube_video_url', 'description']

