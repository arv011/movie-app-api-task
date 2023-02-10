from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from accounts.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from movie.models import GENRE_CHOICES, Movie
from movieCollection.helpers import MovieCollectionHelper
from movieCollection.serializers import MovieCollectionSerializer

# Create your views here.


class MovieCollectionApiView(APIView):
    authentication_class = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request,uuid=None):
        '''Get moviecollection list'''
        response = {"is_success": False, "message": "something went wrong, please try again", "data":{}}
        try:
            uu = uuid if uuid else request.query_params.get('uuid','')
            res,error = MovieCollectionHelper(request,uu=uu).get()
            if res:
                response['data'] = res
                response['message'] = "success"
                response['is_success'] = True
                return Response(response,status=status.HTTP_200_OK)
            
            response['error_list'] = error
        except Exception as e:
            print(e)
        return Response(response,status=status.HTTP_400_BAD_REQUEST)  
    
    def post(self, request):
        '''Create Collection with addition of movies'''
        response = {"status": False, "message": "something went wrong, please try again"}

        try:
            res,error = MovieCollectionHelper(request).update_or_create()
            if res:
                response['collection_uuid'] = res
                response['message'] = "success"
                response['status'] = True
                return Response(response,status=status.HTTP_201_CREATED)
            response['error_list'] = error
        except Exception as e:
            print(e)
        return Response(response,status=status.HTTP_400_BAD_REQUEST)  
    
    def put(self, request,uuid=None):
        '''Update Collection with addition of movies'''
        response = {"status": False, "message": "something went wrong, please try again"}
        uu = uuid if uuid else request.data.get('uuid','')
        try:
            res,error = MovieCollectionHelper(request,uu=uu).update_or_create()
            if res:
                response['collection_uuid'] = res
                response['message'] = "success"
                response['status'] = True
                return Response(response,status=status.HTTP_200_OK)
            response['error_list'] = error
        except Exception as e:
            print(e)
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,uuid=None):
        '''Update Collection with addition of movies'''
        response = {"status": False, "message": "something went wrong, please try again"}
        uu = uuid if uuid else request.query_params.get('uuid','')
        try:
            res,error = MovieCollectionHelper(request,uu=uu).delete()
            if res:
                response['message'] = "collection successully deleted" 
                response['status'] = res
                return Response(response,status=status.HTTP_202_ACCEPTED)
            response['error_list'] = error
        except Exception as e:
            print(e)

        return Response(response,status=status.HTTP_400_BAD_REQUEST)