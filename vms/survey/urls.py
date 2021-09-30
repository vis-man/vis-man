from django.urls import path
from . import views

urlpatterns = [
    path('', views.sites, name='sites'),
    path('survey/sign_out', views.sign_out, name='sign_out'),
    path('survey/<str:pk>/sign_in', views.sign_in, name='sign_in'),
    path('survey/<str:pk>/enter_exit', views.enter_exit, name='enter_exit'),
]