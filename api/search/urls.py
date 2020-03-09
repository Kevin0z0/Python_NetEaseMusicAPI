from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('default', views.default),
    path('suggest', views.suggest),
    path('multimatch', views.multimatch),
    path('hot', views.hot),
    path('hotdetail', views.hotdetail),
]
