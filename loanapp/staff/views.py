from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from client.models import Loans, Payments, Client

# Create your views here.
def test(request):
    print("test view for staff")


@login_required
def staff_dashboard_view(request):
    user = request.user
    loan_requests = Loans.objects.all()
    my_clients = Client.objects.filter(staff=user)
    all_payments = Payments.objects.all()

    return render(request, 'staff/staff_dashboard.html', {
        'loan_requests':loan_requests,
        'my_clients':my_clients,
        'all_payments':all_payments
    })
