from django.core.management.base import BaseCommand
from django.db.models import Count
from survey.models import Visitor, History
from datetime import timedelta, datetime
  
def now():
    return datetime.now()
  
class Command(BaseCommand):
    help = 'Displays stats related to Article and Comment models'
  
    def handle(self, *args, **kwargs):
        From = now() - timedelta(minutes=2)
        To = now()
  
        articles_published_in_last_5_hour = Visitor.objects.filter(
            checkin__gt=From, checkin__lte=To).count()

        print("Articles Published in last 2 min = ",
              articles_published_in_last_5_hour)
        