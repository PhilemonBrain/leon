from django.db import models
from app.models import User
from len_admin.models import Admin
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField('Full Name', max_length=200)
    # email = models.EmailField('Email Addess')
#   # password = models.PasswordField('Password')
    # staff_image = models.ImageField('Profile Picture', upload_to='uploads/staff')
    address = models.CharField('Address', max_length=255)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, blank=True, related_name="branch")
    position = models.CharField('Position', max_length=255, default='Manager')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) 
    # phone_number = models.CharField('Phone Number', default='07069501730') #i dont know if this max value is in buytes or digits?
    added_on = models.DateTimeField(auto_now_add=True)
    add_by = models.ForeignKey(Admin, on_delete=models.CASCADE)

    readonly_fields = [
        'added_on',
    ]


class Branch(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    added_by = models.ForeignKey(Admin, on_delete=models.CASCADE, blank=True, related_name="added_by") #I Set the branch to be added by Admin cos there's a circular loop. If no branch is added, no staff can be added and vice versa
    date_added = models.DateField(default=timezone.now)  
    
    readonly_fields = [
        'date_added',
    ]