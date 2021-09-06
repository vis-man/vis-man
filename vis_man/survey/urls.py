from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='vis-man-home'),
    path('survey/signin', views.sites, name='vis-man-sites'),
    path('survey/signout', views.signout, name='vis-man-signout'),
    path('survey/<int:pk>/', views.forms, name='vis-man-forms')
]