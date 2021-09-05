from django.db import models
from datetime import datetime

class Site(models.Model):
  name = models.CharField(max_length=50, unique=True)
  address = models.CharField(max_length=100)

  def __str__(self):
    return self.name

now = datetime.now()

class Visitor(models.Model):
  visitor_name = models.CharField(max_length=50)
  role = models.CharField(max_length=50)
  email = models.EmailField()
#   phone = models.IntegerField()
  nightstay = models.BooleanField(default=False)
  checkin = models.DateTimeField(default=now.strftime("%Y-%m-%d %H:%M:%S"))
  planned_checkout = models.DateTimeField()
  checkout = models.DateTimeField(null=True, blank=True)
#   induction = models.CharField(max_length=50)
#   emergency_name = models.CharField(max_length=50)
#   emergency_phone = models.IntegerField()
#   emergency_relation = models.CharField(max_length=50)
#   place = models.ForeignKey('Site',on_delete=models.PROTECT, default=1)
  

  def __str__(self):
    return self.visitor_name