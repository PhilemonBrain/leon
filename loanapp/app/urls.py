from .views import login, home
from django.urls import path, re_path

app_name = 'app'

urlpatterns = [
    path("login/", login, name="login"),
    path("home/", home, name='home')
]

