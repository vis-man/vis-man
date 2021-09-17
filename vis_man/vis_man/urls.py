from django.urls import path, include
from survey.admin import vms_admin
urlpatterns = [
    path('admin/', vms_admin.urls),
    path('', include('survey.urls'))
]
