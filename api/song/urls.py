from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('url', views.url),
    path('lyric', views.lyric),
    path('check', views.check),
    path('detail', views.detail),
    path('recommend', views.recommend),
    path('newsong', views.newsong),
    path('simi', views.simi),
    path('top', views.top),
    path('simiuser', views.simiuser),
    path('new', views.new),
    path('like', views.like),
    path('intelligence', views.intelligence),
]
