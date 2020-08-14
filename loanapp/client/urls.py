from .views import client_dashboard_view, new_loan
from django.urls import path, re_path

app_name = 'client'

urlpatterns = [
    path("dashboard/", client_dashboard_view, name='dashboard'),
    path("new_loan/", new_loan, name='new_loan'),
]