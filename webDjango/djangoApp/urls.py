from django.urls import path
from django.urls.converters import PathConverter
from . import views

urlpatterns = [
    path('',views.index,name='index'),
]