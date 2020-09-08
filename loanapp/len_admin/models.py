from django.db import models
# import app.models

# Create your models here.
class Admin(models.Model):
    user = models.OneToOneField('app.User', on_delete=models.CASCADE, related_name='user_admin') #Used the app.User to prevent circular imports
    # is_admin = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"