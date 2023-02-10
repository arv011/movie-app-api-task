from accounts.models import User, RequestCounter
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import transaction
from django.core.exceptions import MultipleObjectsReturned


def get_or_create_user_token(is_user=False,**kwargs):
    '''Get or Create user and generating jwt token'''
    token = None
    username = kwargs.get('username')
    password = kwargs.get('password')
    email = kwargs.get('email') if kwargs.get('email') else kwargs.get('username')
    try:
        if not is_user:
            with transaction.atomic():
                user = User(username=username,email=email)
                user.set_password(make_password(password))
                user.save()
        else:
            user = User.objects.get(username=username,email=email)
        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)
    except Exception as e:
        print(e)
    return token

def get_or_reset_request_counter(reset=False):
    '''get or reset server counter'''
    value = None
    obj = RequestCounter.objects.filter(is_deleted=False).last()
    print(obj)
    if obj:
        if reset: 
            obj.is_deleted = True
            obj.save()
            value = "request count reset successfully"
        else: value = int(obj.counts)
    return value

