from django.urls import path, include
from . import views
urlpatterns = [
    path('list/', views.youtube_list_view, name='home'),
    path('create/', views.youtube_create_view, name='create'),
]


