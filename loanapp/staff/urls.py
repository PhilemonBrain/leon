from .views import test, staff_dashboard_view, add_new_branch, list_staff, add_staff, list_branch, delete_branch, delete_staff
from django.urls import path, re_path

app_name = 'staff'

urlpatterns = [
    path("test/", test, name='test'),
    path("dashboard/", staff_dashboard_view, name='dashboard'),
    path("add_branch/", add_new_branch, name='add_branch'),
    path("add_staff/", add_staff, name='add_staff'),
    path("list_staff/", list_staff, name='list_staff'),
    path("list_branch/", list_branch, name='list_branch'),
    path('delete/<int:id>', delete_branch, name='delete_branch'),
    path('delete_staff/<int:id>', delete_staff, name='delete_staff'),
]