from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('survey.urls')),
    path('vis_man_admin/', include('vis_man_admin.urls'))
]
