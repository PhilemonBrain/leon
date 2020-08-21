from django.contrib import admin
from django.contrib.auth import get_user_model as User
from staff.models import Staff, Branch
from client.models import Client, Payments, Loans
from len_admin.models import Admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

admin.site.register(User())
admin.site.register(Staff)
admin.site.register(Branch)
admin.site.register(Client)
admin.site.register(Payments)
admin.site.register(Loans)
admin.site.register(Admin)

