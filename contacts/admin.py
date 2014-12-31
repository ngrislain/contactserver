from django.contrib import admin
from contacts.models import Person, Address, City

# Register your models here.
admin.site.register(Person)
admin.site.register(Address)
admin.site.register(City)
