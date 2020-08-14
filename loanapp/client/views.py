from django.shortcuts import render, redirect
from client.models import Payments, Loans, Client
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def client_dashboard_view(request, id):
    user = request.user
    #depending on the dashboard design we can hav two or more of the following
    #my_payments of my_current_loan_payments

    my_loans = Loans.objects.filter(client=user).filter(status='AC')
    my_payments = Payments.objects.filter(client=user)
    my_current_loan_payments = Payments.objects.filter(client=user).filter(loan=my_loans)

    return render(request, 'client/client_dashboard.html', {
        'my_payments':my_payments,
        'my_loans':my_loans,
        'my_current_loan_payments':my_current_loan_payments
    })


@login_required
def new_loan(request, id=None):              #here we might have a id==NONE argument so that when a staff wants to reapply the loan
    if request.method == "POST":    #he will call this method and pass in the id and query for the client
        user=request.user
        if id:                       #here the ID will be used to query the db and get the value of the user instance
            user = Client.objects.filter(pk=id)
        pending_loan = Loans.objects.filter(client=user).filter(status='PE')
        active_loan = Loans.objects.filter(client=user).filter(status='AC')
        if pending_loan or active_loan:
            print("Error. Pending or active")
        else:
            new_loan = Loans.objects.create(
                user = user,
                status = 'PE',
                loan_amount = request.POST['loan_amount']
            )
            new_loan.save()
            #Write email and sms Notificaations to selected staff and client
            return redirect('client:dashboard')