from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('song', views.song),
    path('album', views.album),
    path('album/new', views.album_new),
    path('album/detail', views.album_detail),
    path('album/dynamic', views.album_dynamic),
    path('album/sub', views.album_sub),
    path('album/sublist', views.album_sublist),
    path('desc', views.desc),
    path('mv', views.mv),
    path('top', views.top),
    path('simi', views.simi),
    path('lists', views.lists),
    path('sub', views.sub),
    path('sublist', views.sublist),
    path('topsong', views.topsong),
    path('toplist', views.toplist),
]
