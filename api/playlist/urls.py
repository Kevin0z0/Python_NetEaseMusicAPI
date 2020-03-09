from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('detail', views.detail),
    path('recommend', views.recommend),
    path('personalized', views.personalized),
    path('simi', views.simi),
    path('related', views.related),
    path('subscribe', views.subscribe),
    path('subscribers', views.subscribers),
    path('tracks', views.tracks),
    path('create', views.create),
    path('delete', views.delete),
    path('catlist', views.catlist),
    path('hot', views.hot),
    path('top', views.top),
    path('tophigh', views.tophigh),
    path('update', views.update),
    path('update/desc', views.update_desc),
    path('update/name', views.update_name),
    path('update/tags', views.update_tags),
]
