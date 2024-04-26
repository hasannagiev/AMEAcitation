from django.contrib import admin
from .models import Profile, ProfileUpdate, Employee, EmailAddress, PhoneNumber, Institution, Department, Division ,EmploymentHistory
admin.site.register(Institution)
admin.site.register(Department)
admin.site.register(Division)
#admin.site.register(Profile)
admin.site.register(ProfileUpdate)

class EmailAddressInline(admin.TabularInline):
    model = EmailAddress

class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber

class EmploymentHistoryInline(admin.TabularInline):
    model = EmploymentHistory

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [EmailAddressInline, PhoneNumberInline,EmploymentHistoryInline]
    list_filter = ('first_name', 'second_name')

admin.site.register(Employee, EmployeeAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_filter = ['platform']

admin.site.register(Profile, ProfileAdmin)