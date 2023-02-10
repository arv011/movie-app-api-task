from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from accounts.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from movie.helpers import get_movies_credy_api

# Create your views here.

class MovieApiView(APIView):
    authentication_class = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        '''Get movies list view'''
        response = {"status": False, "message": "something went wrong, please try again"}
        try:
            page = request.query_params.get('page')
            url = request.query_params.get('url')
            res = get_movies_credy_api(url=url, page=page)
            if res:
                response = res
                return Response(response,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)

        return Response(response,status=status.HTTP_400_BAD_REQUEST)  

        