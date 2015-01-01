from django.db import models

# Create your models here.
class Person(models.Model):
    title = models.CharField(max_length=8, null=True, blank=True, choices=(('M', 'M'), ('MME', 'Mme'), ('MLLE', 'Mlle')))
    first_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256, null=True, blank=True)
    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.last_name)

class Info(models.Model):
    person = models.OneToOneField('Person', related_name='info')
    birth_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return u'Info about {}'.format(self.person)

class Member(models.Model):
    person = models.OneToOneField('Person', related_name='member')
    groups = models.ManyToManyField('Group', blank=True, related_name='members')
    def __unicode__(self):
        return u'Member {}'.format(self.person)

class Address(models.Model):
    person = models.ForeignKey('Person', related_name='addresses')
    content = models.CharField(max_length=256)
    city = models.ForeignKey('City', null=True, blank=True)
    country = models.ForeignKey('Country', null=True, blank=True)
    def __unicode__(self):
        return u'Address of {}'.format(self.person)

class City(models.Model):
    name =  models.CharField(max_length=256)
    country = models.ForeignKey('Country', null=True, blank=True)
    def __unicode__(self):
        return u'{}'.format(self.name)

class Country(models.Model):
    name =  models.CharField(max_length=256)
    def __unicode__(self):
        return u'{}'.format(self.name)

class Email(models.Model):
    person = models.ForeignKey('Person', related_name='emails')
    name = models.CharField(max_length=256, default='Principal', null=True, blank=True)
    address = models.EmailField(max_length=256)
    def __unicode__(self):
        return u'Email of {} ({})'.format(self.person, self.address)

class Phone(models.Model):
    person = models.ForeignKey('Person', related_name='phones')
    name = models.CharField(max_length=256, default='Principal', null=True, blank=True)
    number = models.CharField(max_length=256)
    def __unicode__(self):
        return u'Phone of {} ({})'.format(self.person, self.number)

class Account(models.Model):
    person = models.ForeignKey('Person', related_name='accounts')
    name = models.CharField(max_length=256, default='Twitter', null=True, blank=True)
    address = models.CharField(max_length=256)
    def __unicode__(self):
        return u'{} of {} ({})'.format(self.name, self.person, self.address)

class Group(models.Model):
    name = models.CharField(max_length=256, default='Group', null=True, blank=True)
    def __unicode__(self):
        return u'{}'.format(self.name)
