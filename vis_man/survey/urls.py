from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='vis-man-home'),
    path('Gingin-Gravity-Precinct', views.gingin, name='gingin'),
    path('IOMRC-Crawley', views.iomrc, name='iomrc'),
    path('Watermans-Bay', views.watermans, name='watermans'),
    path('Ridgefield-Farm', views.ridgefield, name='ridgefield')
]
