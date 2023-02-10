from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from accounts.models import User
from rest_framework.test import APIClient
from rest_framework.test import APITestCase


class APITESTCaseK(APITestCase):
    
    def setUp(self):
        super(APITESTCaseK, self).setUp()
        self.username = "testuser@yopmail.com"
        self.password = "Insure@12"
        self.email = "testuser@yopmail.com"
        self.user = User.objects.create(username=self.username, email=self.email,
                                        is_active=True)
        self.user.set_password(make_password(self.password))
        self.user.save()
        self.client = APIClient()


    def get_client(self):
        client = APIClient()
        return client
    
    def get_user_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)

    def register_user(self):
        url = '/register/'
        payload = {"username": 'testuser2@yopmail.com','password':'Insure@12'}
        response = self.client.post(url,data=payload)
        return response