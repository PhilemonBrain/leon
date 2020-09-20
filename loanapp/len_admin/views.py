from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model as User
from django.contrib import messages
from len_admin.models import Admin
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required
def dashboard(request):
    user = request.user
    try:
        Admin.objects.get(user=user.id) #check if user exists in the Admin model
        return render(request, 'len_admin/admin_dashboard.html')
    except ObjectDoesNotExist:
        return redirect("app:logout")


@login_required
def add_admin(request):
    users = request.user
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 == pass2:
            password = pass1
            if User().objects.filter(email=email).exists():
                messages.info(request, 'Email already exists.')
            else:
                user = User()(email=email)
                user.first_name = first_name
                user.last_name = last_name
                user.phonenumber = phonenumber
                user.set_password(password)
                user.is_admin = True
                user.save(commit=False)
                admin = Admin.objects.create(user=user)
                user.save()
                admin.save()
                messages.success(request, "Admin successfully added")
            #check logged in user and render the current add-staff page for the proper user. I wouldn't want to redirect admin to staff signup page
            return render(request, "len_admin/add_admin.html")
        else:
            messages.error(request, 'Passwords do not match')
    elif request.method == 'GET':
        try:
            Admin.objects.get(user=users.id) #checks if the logged in user is an Admin
            return render(request, "len_admin/add_admin.html")
        except ObjectDoesNotExist:
            return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
#confirm that logged in user is an admin or staff and not ordinary user
def list_admin(request):
    user = request.user
    if request.method == "GET":
        try:
            Admin.objects.get(user=user.id) #checks if the logged in user is an Admin
            admins = Admin.objects.all()
            context = {'admins' : admins,}
            return render(request, "len_admin/list_admin.html", context)
        except ObjectDoesNotExist:
            return redirect(request.META.get('HTTP_REFERER', '/'))  #Does not work as expected.    
    # return render(request, "len_admin/list_admin.html")