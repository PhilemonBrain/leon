from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

# Create your models here.

class MyManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        
        if not email:
            raise ValueError("Email is required")

        user = self.model(
            email = self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email adress', max_length=255, unique=True)
    # category = models.CharField(max_length=255, default="Client")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyManager()

    def __str__(self):
        return f'{self.email}, {self.category}'


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField('Full Name', max_length=200)
    # email = models.EmailField('Email Addess')
#   # password = models.PasswordField('Password')
    # staff_image = models.ImageField('Profile Picture', upload_to='uploads/staff')
    branch = models.CharField('Branch', max_length=255, default='Asaba')
    position = models.CharField('Position', max_length=255, default='Manager')
    phone_number = models.IntegerField('Phone Number', default='07069501730') #i dont know if this max value is in buytes or digits?


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField('Full Name', max_length=200)
    # email = models.EmailField('Email Address')
    # password = models.PasswordField('Password')
    # dob = models.DateField('Date Of Birth', default=date.today)
    # client_image = models.ImageField('Profile Picture', upload_to='uploads/clients')
    # loan_amount = models.IntegerField('Loan Amount')
    # loan_balance = models.IntegerField('Loan Amount')
    # loan_date = models.DateField('Loan Approval Date', default=date.today)
    # phone_number = models.IntegerField('Phone Number') #i dont know if this max value is in buytes or digits?
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.email} {self.id}"



class Payments(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # pay_date = models.DateField('Date Of Payment', default=date.today)
    amount_paid = models.IntegerField('Amount Paid')
    # p_paid = models.IntegerField('Principal Paid')
    # i_paid = models.IntegerField('Interest Paid')
    bal_left = models.IntegerField('Balance Outstanding')
    # pay_receipt = models.ImageField('Payment Receipt', upload_to='uploads/receipts')

    def __str__(self):
        return f"{self.client}, {self.amount_paid}"
    # def __str__(self):
    #     return f"{self.pay_date},  {self.amount_paid}, {self.bal_left} "
