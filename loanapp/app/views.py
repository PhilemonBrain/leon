from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    print("in login")
    print(request.POST.get("email"))
    print(request.POST.get("password"))
    print(request.method)
    if request.method == "POST":
        print("in request")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(f'email: {email}, password: {password}')
        user = auth.authenticate(email=email, password=password)
        print(user)
        if user:
            print(user)
            auth.login(request, user)
            return redirect("app:home")
    return render(request, "app/login.html")


@login_required(login_url="/login")        
def home(request):
    # user = request.user
    return render(request, "app/home.html")