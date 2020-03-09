from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('song', views.song),
    path('album', views.album),
    path('playlist', views.playlist),
    path('dj', views.dj),
    path('video', views.video),
    path('mv', views.mv),
    path('hot', views.hot),
    path('event', views.event),
    path('like', views.like),
]
