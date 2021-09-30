from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class AdminConfig(AdminConfig):
    default_site = 'survey.admin.AdminArea'

class SurveyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'survey'
