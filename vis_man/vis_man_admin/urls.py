from django.urls import path

from . import views

urlpatterns = [
    # /vis_man_admin/
    path('', views.login, name = 'vis-man-admin-login'), 
    # /vis_man_admin/home/
    path('home/', views.home, name = 'vis-man-admin-home')
    
]