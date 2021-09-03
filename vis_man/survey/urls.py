from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='vis-man-home'),
    path('<str:pk>/', views.sites, name='site')
]
