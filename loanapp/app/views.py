from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model as User
from django.contrib import messages
from client.models import Payments, Client, Loans
from staff.models import Staff
import datetime
# Create your views here.


# def apply_for_loan(request):     #profile must be complete before a loan can be applied. Loan model
#     loan_amount = request.POST.get("loanamount")
    #Guarantors Details
    # Gname = request.POST.get("guarantor_name")
    # Gaddress = request.POST.get("guarantor_address")
    # Gphone = request.POST.get("guarantor_phone")
    # monthly_salary = request.POST.get("salary")
    # client = Client.objects.get(user=request.user)
    # loan = Loans(
    #     user = client,
    #     loan_amount = loan_amount,
    #     apply_date = datetime.date.today
    #     .........etc
    # )


# def approve_loan(request, loan_id):
#     loan = Loans.objects.get(id=loan_id)
#     loan.status = "AP"
#     staff = Staff.objects.get(user=request.user)
#     loan.approved_by = staff
#     loan.date_approved = datetime.date.today
#     laon.save()


# def complete_profile(request): #prerequisite to apply for loan. Should match the CLIENT models
#     nationality = 
#     pob = place of birth
#     dob = date of birth
#     soo = state of origin
#     House_address = 
#     Office_address = 
#     client = Client(
#         user = request.user,
#         soo = soo,
#         dob = dob
#         ........etc
#     )



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
                return redirect("staff:dashboard")
            elif user.is_admin:
                return redirect("len_admin:dashboard")
            else:
                return redirect("app:home")
        else:
            print("Wrong password")
    return render(request, "app/login.html")


@login_required         
def home(request):
    payments = Payments.objects.all()
    return render(request, "staff/staff_dashboard.html", {
        "payments":payments
    })


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









