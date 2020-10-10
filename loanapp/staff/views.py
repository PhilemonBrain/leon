from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from client.models import Loans, Payments, Client
from staff.models import Staff, Branch
from len_admin.models import Admin
from app.models import User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

# Create your views here.
def test(request):
    print("test view for staff")


@login_required
def staff_dashboard_view(request):
    user = request.user
    loan_requests = Loans.objects.all()
    # my_clients = Client.objects.filter(staff=user)
    all_payments = Payments.objects.all().order_by('id')

    # working with multiple paginations ona a single page??

    paginator = Paginator(all_payments, 2)
    # paginator2 = Paginator(loan_requests, 2)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)


    context = {
        'loan_requests':loan_requests,
        'page':page,
        # 'my_clients':my_clients,
        'all_payments':all_payments
    }

    return render(request, 'staff/staff_dashboard.html', context)


@login_required
def clients(request):
    all_clients = Client.objects.all().order_by('id')

    paginator = Paginator(all_clients, 2)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)

    context = {
        'page' : page
    }
    
    return render(request, 'staff/staff_clients.html', context)


@login_required
def payments(request):
    all_payments = Payments.objects.all()
    return render(request, 'staff/staff_payments.html', {
        'all_payments':all_payments
    })


@login_required
#confirm that logged in user is a staff or admin and not ordinary user
def add_staff(request):
    user = request.user
    branches = Branch.objects.all()
    context = {
        'branches' : branches
    }
    if request.method == 'POST':
        try:
            admin = Admin.objects.get(user=user.id)#checks if logged in user is admin
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            email = request.POST.get('email')
            phonenumber = request.POST.get('phonenumber')
            branch = Branch.objects.get(pk=request.POST.get('branch'))
            # branch = request.POST.get('branch')
            # branch = get_object_or_404(Branch, pk=request.POST.get('branch'))
            position = request.POST.get('position')
            address = request.POST.get('address')
            pass1 = request.POST.get('pass1')
            pass2 = request.POST.get('pass2')
            # username = first_name+"."+last_name
            if pass1 == pass2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email already exists.')
                # elif User.objects.filter(username=username).exists():
                #     messages.info(request, 'Username already exists.')
                else:
                    user = User(email=email)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.phonenumber = phonenumber
                    # user.username = username
                    user.is_staff = True
                    user.set_password(pass1)
                    user.save(commit=False)
                    staff = Staff.objects.create(user=user, branch=branch, position=position, address=address, phone_number=phonenumber, add_by = admin)
                    user.save()
                    staff.save()
                    messages.success(request, "Staff successfully added")
                #check logged in user and render the current add-staff page for the proper user. I wouldn't want to redirect admin to staff signup page
                return render(request, "staff/add_staff.html", context)
            else:
                messages.error(request, 'Passwords do not match')
        except ObjectDoesNotExist:
            messages.error(request, 'Unauthorised access')
    return render(request, "staff/add_staff.html", context)

@login_required
#confirm that logged in user is an admin and not ordinary user
def delete_staff(request, id):
    user = request.user
    if request.method == "GET":
        try:
            staff = Staff.objects.get(id=id)
            if staff.user.id == user.id:
                messages.warning(request, "Ode! You can't delete yourself")
            else: 
                staff_active = User.objects.get(id=staff.user.id)
                staff_active.is_active = False
                staff_active.save()
                # staff.delete()
                messages.success(request, "Staff successfully deleted!")
                #Go back to staff listing page
                return redirect("staff:list_staff")
        except ObjectDoesNotExist:
            messages.warning(request, "Staff does not exists")
    return render(request, 'staff/list_staff.html')

@login_required
#confirm that logged in user is an admin and not ordinary user
def delete_branch(request, id):
    user = request.user
    if request.method == "GET":
        try:
            branch = Branch.objects.get(id=id)
            try:
                Admin.objects.get(user=user.id) #check if logged in user is an admin
                branch.delete()
                messages.success(request, "Branch deleted successfully")
                return redirect("staff:list_branch")
            except ObjectDoesNotExist:
                messages.warning(request, "Unauthorised access")
                # return render(request, 'staff/list_branch.html')
        except ObjectDoesNotExist:
            messages.warning(request, "Branch does not exist")
    return render(request, 'staff/list_branch.html')


@login_required
#confirm that logged in user is an admin or staff and not ordinary user
def add_new_branch(request):
    user = request.user 
    name = request.POST.get('name')
    address = request.POST.get('address') 
    if request.method == "POST":
        try:
            admin = Admin.objects.get(user=user.id)#checks if logged in user is admin
            # if staff.is_active == True:
            # if staff.user.id == user.id:
            added_by = admin 
            branch = Branch.objects.create(name=name, address=address, added_by=added_by)
            branch.save()
            messages.success(request, "Branch successfully added")
            # else:
            #     messages.warning(request, "User account not found")
        except ObjectDoesNotExist:
            messages.warning(request, "Unauthorised access")
    return render(request, "staff/add_branch.html")


@login_required
#confirm that logged in user is an admin or staff and not ordinary user
def list_staff(request):
    user = request.user
    if request.method == "GET":
        try:
            Staff.objects.get(user=16) #checks if the logged in user is an Admin
            staffs = User.objects.filter(is_staff=True, is_active=True).values_list('id', flat=True)
            staff =  Staff.objects.filter(user__in=staffs)
            context = {'staff' : staff}
            return render(request, "staff/list_staff.html", context)
        except ObjectDoesNotExist:
            # return redirect(request.META.get('HTTP_REFERER', '/'))
            return render(request, "staff/list_staff.html")     
    return render(request, "staff/list_staff.html", context)

@login_required
#confirm that logged in user is an admin or staff and not ordinary user
def list_branch(request):
    user = request.user
    if request.method == "GET":
        try:
            Staff.objects.get(user=user.id) #checks if the logged in user is a staff. Update to check for admin as well
            branches = Branch.objects.all()
            context = {'branches' : branches,}
            return render(request, "staff/list_branch.html", context)
        except ObjectDoesNotExist:
            return redirect(request.META.get('HTTP_REFERER', '/')) 
    return redirect(request.META.get('HTTP_REFERER', '/')) #Not sure why I added this again