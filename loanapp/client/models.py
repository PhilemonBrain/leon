from django.db import models
from app.models import User
from staff.models import Staff
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    loan_amount = models.IntegerField('Loan Amount')
    loan_balance = models.IntegerField('Loan Balance', null=True)
    # soo = State of Origin
    # dob = models.DateField('Date Of Birth', default=date.today)
    # nationality = nationality
    # place_of_birth = place_of_birth
    # house_address = house_address
    # monthly_salary = monthly_salary
    # client_image = models.ImageField('Profile Picture', upload_to='uploads/clients')
    # loan_date = models.DateField('Loan Approval Date', default=date.today)
    # phone_number = models.IntegerField('Phone Number') #i dont know if this max value is in buytes or digits?
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"

class Payments(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # pay_date = models.DateField('Date Of Payment', default=date.today)
    amount_paid = models.IntegerField('Amount Paid')
    # p_paid = models.IntegerField('Principal Paid')
    # i_paid = models.IntegerField('Interest Paid')
    bal_left = models.IntegerField('Balance Outstanding')
    # pay_receipt = models.ImageField('Payment Receipt', upload_to='uploads/receipts')
    # loan = models.ForeignKey(Loans, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.client}, {self.amount_paid}"
    # def __str__(self):
    #     return f"{self.pay_date},  {self.amount_paid}, {self.bal_left} "


class Loans(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)     #@kene wetin we go do on_delete
    apply_date = models.DateField(default=timezone.now)
    approved_by = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, related_name="approved_by")  #@kene wetin we go do on_delete
    # date_approved  = models.DateField(null=True)
    closed_by = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, related_name="closed_by", null=True)  #@kene wetin we go do on_delete
    loan_amount = models.IntegerField('Loan Amount', null=True) #w
    PENDING='PE'
    ACTIVE='AC'
    CLOSED='CL'
    APPROVED='AP'
    LOAN_STATUS = [
        (PENDING, 'PE'),
        (ACTIVE, 'AC'),
        (CLOSED, 'CL'),
        (APPROVED, 'AP'),
    ]
    status = models.CharField(max_length=2, choices=LOAN_STATUS)
    #Guarantors Details
    # Gname = request.POST.get("guarantor_name")
    # Gaddress = request.POST.get("guarantor_address")
    # Gphone = request.POST.get("guarantor_phone")
    # monthly_salary = request.POST.get("salary")

    def __str__(self):
        return f"{self.user}, {self.user.loan_amount}"