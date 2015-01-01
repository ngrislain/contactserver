from django.contrib import admin
from contacts.models import Person, Info, Member, Address, City, Country, Email, Phone, Account, Group

class InfoInline(admin.StackedInline):
    model = Info
    extra = 1

class MemberInline(admin.StackedInline):
    model = Member
    extra = 1
    filter_horizontal = ('groups',)

class AddressInline(admin.TabularInline):
    model = Address
    extra = 0

class EmailInline(admin.TabularInline):
    model = Email
    extra = 0

class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0

class AccountInline(admin.TabularInline):
    model = Account
    extra = 0

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_groups')
    inlines = [AddressInline, EmailInline, PhoneInline, AccountInline, InfoInline, MemberInline]
    
    def get_groups(self, obj):
        return "\n".join([grp.name for grp in obj.groups.all()])

#class MemberAdmin(admin.ModelAdmin):
#    filter_horizontal = ('groups',)

# Register your models here.
admin.site.register(Person, PersonAdmin)
#admin.site.register(Member, MemberAdmin)
#admin.site.register(Info)
#admin.site.register(Address)
#admin.site.register(City)
#admin.site.register(Country)
#admin.site.register(Email)
#admin.site.register(Phone)
#admin.site.register(Account)
admin.site.register(Group)
