from django.urls import path
from . import views

urlpatterns  = [
    path('',views.predicator, name='prdictor'),
    
]