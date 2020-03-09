from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('private', views.private),
    path('history', views.history),
    path('sendmsg', views.sendmsg),
    path('comment', views.comment),
    path('forwards', views.forwards),
    path('notices', views.notices),
]
