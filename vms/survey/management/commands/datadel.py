from django.core.management.base import BaseCommand
from django.db.models import Q
from survey.models import Visitor, History
from datetime import timedelta, datetime
  
def now():
    return datetime.now()
  
class Command(BaseCommand):
    help = 'Removes visitors and histories older than 3 years (1095 days)'
  
    def handle(self, *args, **kwargs):
        From = now() - timedelta(days=1095)
        To = now()
  
        Visitor.objects.filter(~Q(checkin__gt=From, checkin__lte=To)).delete()
        History.objects.filter(~Q(checkin__gt=From, checkin__lte=To)).delete()
        
        return
        
    