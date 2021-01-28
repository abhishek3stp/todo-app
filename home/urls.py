from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('createtask/', views.createTask, name='createtask'),
    path('deletetask/<str:slug>/', views.deleteTask, name='deletetask'),
]