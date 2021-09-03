from django.db import models

class Site(models.Model):
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=100)

  def __str__(self):
    return self.name


class Form(models.Model):
  name = models.CharField(max_length=50)
  role = models.CharField(max_length=50)
  email = models.EmailField()
  phone = models.IntegerField()
  nightstay = models.BooleanField(default=False)
  arrival = models.DateField()
  departure = models.DateField()
  induction = models.CharField(max_length=50)
  emergency_name = models.CharField(max_length=50)
  emergency_phone = models.IntegerField()
  emergency_relation = models.CharField(max_length=50)

  def __str__(self):
    return self.name