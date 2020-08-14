from django.contrib import admin
from django.contrib.auth import get_user_model as User
from .models import Staff
from client.models import Client, Payments, Loans
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

admin.site.register(User())
admin.site.register(Staff)
admin.site.register(Client)
admin.site.register(Payments)
admin.site.register(Loans)
