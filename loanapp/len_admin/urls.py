from .views import test
from django.urls import path, re_path

app_name = 'admin'

urlpatterns = [
    path("test/", test, name='test'),
]