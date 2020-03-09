from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('url', views.url),
    path('detail', views.detail),
    path('lists', views.lists),
    path('group', views.group),
    path('related', views.related),
    path('sub', views.sub),
]
