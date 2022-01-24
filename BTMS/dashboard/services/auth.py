


from multiprocessing import AuthenticationError
from dashboard.models import Users
from django.contrib.auth import hashers


def authenticate_user(username: str, raw_password_to_check: str) -> Users:
    user: Users = Users.objects.filter(username=username).first()

    if user is not None:
        if user.check_password(raw_password_to_check):
            return user

    raise AuthenticationError(username, '')

