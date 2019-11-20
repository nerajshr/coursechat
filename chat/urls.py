# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),

]



















# from django.urls import path, re_path


# from .views import ThreadView, InboxView

# app_name = 'chat'
# urlpatterns = [
#     path("", InboxView.as_view()),
#     re_path(r"^(?P<username>[\w.@+-]+)", ThreadView.as_view()),
# ]
