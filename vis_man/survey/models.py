from django.db import models

class Site(models.Model):
  name = models.CharField(max_length=50, unique=True)
  address = models.CharField(max_length=100)

  def __str__(self):
    return self.name


class Visitor(models.Model):
  visitor_name = models.CharField(max_length=50)
  role = models.CharField(max_length=50)
  email = models.EmailField()
#   phone = models.IntegerField()
  nightstay = models.BooleanField(default=False)
  checkin = models.DateTimeField(auto_now_add=True)
  planned_checkout = models.DateTimeField()
  checkout = models.DateTimeField(null=True, blank=True)
#   induction = models.CharField(max_length=50)
#   emergency_name = models.CharField(max_length=50)
#   emergency_phone = models.IntegerField()
#   emergency_relation = models.CharField(max_length=50)
#   place = models.ForeignKey('Site',on_delete=models.PROTECT, default=1)
  

  def __str__(self):
    return self.visitor_name