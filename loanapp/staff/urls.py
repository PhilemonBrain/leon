from .views import test
from django.urls import path, re_path

app_name = 'staff'

urlpatterns = [
    path("test/", test, name='test'),
]