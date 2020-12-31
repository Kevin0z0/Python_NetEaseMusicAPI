from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('user/', include('api.user.urls')),
    path('song/', include('api.song.urls')),
    path('playlist/', include('api.playlist.urls')),
    path('artists/', include('api.artists.urls')),
    path('tasks/', include('api.tasks.urls')),
    path('dj/', include('api.dj.urls')),
    re_path(r'^search[/]*', include('api.search.urls')),
    path('mv/', include('api.mv.urls')),
    re_path(r'^comment[/]*', include('api.comment.urls')),
    path('video/', include('api.video.urls')),
    path('msg/', include('api.msg.urls')),
    path('hot', views.hot),
    path('hotcomment', views.hotcomment),
    path('banner', views.banner),
    path('private', views.private),
    path('toplist', views.toplist),
    path('toplists', views.toplists),
    path('toplist/detail', views.toplist_detail),
]
