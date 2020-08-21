from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model as User
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        # user = User().objects.filter(email=email).filter(password=password)
        # print(f'after query is :{user}')
        # print(f'email: {email}, password: {password}')
        user = auth.authenticate(email=email, password=password)
        if user:
            auth.login(request, user)
            if user.is_staff:
                return redirect("staff:staff_dashboard_view")
            elif user.is_admin:
                return redirect("len_admin:dashboard")
            else:
                return redirect("app:home")
        else:
            print("Wrong password")
    return render(request, "app/login.html")


@login_required         
def home(request):
    # user = request.user
    # print(user)
    return render(request, "app/home.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        confirm_pass = request.POST.get('confirmpwd')
        password = request.POST.get('pwd')
        if password == confirm_pass:
            if User().objects.filter(email=email).exists():
                messages.info(request, 'Email Taken, Please try again')
                return redirect('app:signup')
            else:
                user = User()(email=email)
                user.first_name = first_name
                user.last_name = last_name
                user.phonenumber = phonenumber
                user.set_password(password)
                # user.password = password 
                user.save()
                print(f"user saved. Instance is :{user}")
                return redirect('app:login')
        else:
            messages.error(request, 'Password mismatch')
            return redirect("app:signup")
    return render(request, "app/signup.html")

@login_required
def logout(request):
    auth.logout(request)
    return redirect("app:login")









