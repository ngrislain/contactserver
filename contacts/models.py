from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

class Address(models.Model):
    first_name = models.CharField(max_length=200)
    city = models.ForeignKey('City')

class City(models.Model):
    name =  models.CharField(max_length=200)
