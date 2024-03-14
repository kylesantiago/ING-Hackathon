from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('newjob/', views.newjob, name='newjob'),
    path('candidate/', views.candidate, name='candidate'),
    path('candidates/', views.candidates, name='candidates'),
    path('test/', views.test, name='test'),
]