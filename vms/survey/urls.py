from django.urls import path
from . import views

urlpatterns = [
    path('', views.sites, name='sites'),
    path('survey/signout', views.signout, name='signout'),
    path('survey/<str:pk>/', views.forms, name='forms'),
    path('survey/<str:pk>/enter_exit', views.enter_exit, name='enter_exit'),
]