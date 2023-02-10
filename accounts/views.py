from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from accounts.models import User, RequestCounter
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.serializers import RegisterUserSerializer, LoginUserSerializer
from accounts.helpers import get_or_create_user_token,get_or_reset_request_counter
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

# Create your views here.


class FirstPage(APIView):

    def post(self, request):
        return self.first_page(request)
    
    def get(self,request):
        return self.first_page(request)

    def first_page(self,request):
        '''return landing reponse'''
        response = {"message":'Welcome to movie app, please register yourself',"status":True}
        return Response(response,status=status.HTTP_200_OK)


class RegiterApiView(CreateAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        '''register use by email & password | return: token'''
        response = {"status": False, "message": "something went wrong, please try again"}
        resp = super().create(request, *args, **kwargs)
        token = get_or_create_user_token(is_user=True,**resp.data)
        if token:
            response["status"] = True   
            response["message"] = "success"
            response["access_token"] = token
            return Response(response,status=status.HTTP_201_CREATED)  
           
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
        

class LoginApiView(APIView):

    def post(self, request):
        '''login user by email & password | return: token'''
        response = {"status": False, "message": "something went wrong, please try again","error_list": {}}
        try:
            serializer = LoginUserSerializer(context = {'request': request},data = request.data)
            if serializer.is_valid():
                response["status"] = True
                response["message"] = "success"
                response["access_token"] = serializer.data['access_token']
                return Response(response,status=status.HTTP_200_OK)
            else:
                response["error_list"] = serializer.errors
        except Exception as e:
            print(e)

        return Response(response,status=status.HTTP_400_BAD_REQUEST)  


class RequestCounterResetApiView(APIView):
    authentication_class = [JWTAuthentication]
    permission_classes = (IsAuthenticated,IsAdminUser)
    
    def post(self, request):
        '''reset counter obj | return: Message'''
        response = {"status": False, "message": "something went wrong, please try again"}
        try:
            res = get_or_reset_request_counter(reset=True)
            if res:
                response["status"] = True
                response["message"] = res
                return Response(response,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
        return Response(response,status=status.HTTP_400_BAD_REQUEST)         
    

class RequestCounterApiView(APIView):
    authentication_class = [JWTAuthentication]
    permission_classes = (IsAuthenticated,IsAdminUser)
    
    def get(self, request):
        ''' get counter obj | return: counts'''
        response = {"status": False, "message": "something went wrong, please try again"}
        try:
            res = get_or_reset_request_counter()
            if res:
                response["status"] = True
                response["message"] = 'success'
                response['requests'] = res
                return Response(response,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
        return Response(response,status=status.HTTP_400_BAD_REQUEST)         
