from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('villan',views.big_shot,name='villan'),
    path('character',views.charater,name='character')
]