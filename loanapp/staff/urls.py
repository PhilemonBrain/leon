from .views import test, staff_dashboard_view
from django.urls import path, re_path

app_name = 'staff'

urlpatterns = [
    path("test/", test, name='test'),
    path("dashboard/", staff_dashboard_view, name='dashboard'),
]