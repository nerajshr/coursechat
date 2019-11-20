from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from .models import Youtube
from .forms import YoutubeModelForm
def youtube_list_view(request, *args, **kwargs):
    object_list = Youtube.objects.all()
    return render(request,'./coursechat/home.html', {'object_list':object_list})


def youtube_create_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = YoutubeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = YoutubeModelForm()
    return render(request, './coursechat/form.html', {'form': form})
