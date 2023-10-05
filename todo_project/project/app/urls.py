from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.demo,name='demo'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update')
]