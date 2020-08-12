from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model as User

class EmailAuthBackend(BaseBackend):

    def authenticate(self, request, **kwargs):
        try:
            if request.GET('next') == '/admin/' and request.POST.get("email"):
                email = request.POST.get("email")
                password = request.POST.get("password")
                try:
                    user = User().objects.get(email=email)
                    if user.is_super_user:
                        print("A Super User is logging in")
                        return user
                except User().DoesNotExist:
                    print("User does not exist or user is not a super user")
                    return None
        except:
            pass

        email = kwargs['email']
        password = kwargs['password']
        if email and password:
            # try:
            #     user = User().objects.get(email=email)
            #     print(f"the user password {user.password}")
            #     print(f"the user login password {password}")
            #     if user.check_password(password, user.password):
            #         return user
            #     # check = user.check_password(password)
            #     # print(check)
            #     # if check:
            #     # if password == user.password:
            #     #     return user
            # except User().DoesNotExist:
            #     return None
            try:
                user = User().objects.get(email=email)
            except User().DoesNotExist:
                return None
            else:
                if user.check_password(password):
                    return user
            return None

    
    def get_user(self, user_id):
        try:
            User().objects.get(pk=user_id)
        except User().DoesNotExist:
            return None
