from .views import dashboard, add_admin, list_admin
from django.urls import path, re_path

app_name = 'admin'

urlpatterns = [
    path("", dashboard, name='dashboard'),
    path("add_admin/", add_admin, name='add_admin'),
    path("list_admin/", list_admin, name='list_admin'),
]