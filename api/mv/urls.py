from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('all', views.all),
    path('new', views.new),
    path('netease', views.netease),
    path('recommend', views.recommend),
    path('simi', views.simi),
    path('top', views.top),
    path('detail', views.detail),
    path('url', views.url),
    path('sub', views.sub),
    path('sublist', views.sublist),
]
