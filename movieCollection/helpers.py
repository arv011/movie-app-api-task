from movie.models import GENRE_CHOICES, Movie
from movieCollection.models import UserMovieCollection
from accounts.models import User
from movieCollection.serializers import MovieCollectionSerializer, MovieSerializer
from django.db import transaction
from itertools import islice


class MovieCollectionHelper:
    
    def __init__(self, request,uu=None):
        self.user = request.user 
        self.request = request
        self.uu = uu
        
    def get_user_collections(self,uu=None):
        '''user collection based on uu and owner'''
        data = {'uuid':uu} if uu else {'owner': self.user}
        queryset = UserMovieCollection.objects.filter(**data).prefetch_related('movies')
        return queryset
    
    def get_favourite_genres(self,collections):
        '''return top three favourite genres logic'''
        fav_genres = []
        genre_dict = {}
        try:
            genres = collections.values_list('movies__genres')
            if genres:
                for genre in genres:
                    if genre:
                        for category in genre[0]:
                            if category in genre_dict: genre_dict[category] += 1
                            else: genre_dict[category] = 1
                
                genre_dict = dict(sorted(genre_dict.items(), key=lambda x:x[1], reverse=True))
                if len(genre_dict)<=3:fav_genres = list(genre_dict.key())
                else: fav_genres = list(islice(genre_dict.keys(),3))
        except Exception as e:
            print(e)
        return fav_genres
    
    def update_movie_in_collection(self,uu,obj_list=[]):
        '''update movies in collection'''
        if uu and obj_list:
            collection = self.get_user_collections(uu=uu)
            collection = collection.first()
            collection.movies.add(*obj_list)
        return True
    
    def bulk_create_movies(self,json_dict):
        '''create update movies in model:Movie'''
        movie_list = []
        user_id = self.user.id
        if json_dict:
            for movie in json_dict: 
                movie.update({"genres":movie.get("genres",'').split(','),
                            "updated_by":user_id,"created_by":user_id})
                obj,created = Movie.objects.update_or_create(**movie)
                movie_list.append(obj)
                # movie_list.append(Movie(**movie))
            # movie_list = Movie.objects.bulk_create(movie_list,ignore_conflicts=True)
        return movie_list

    def update_or_create(self):
        '''Method to create or update movie collection'''

        request_data = self.request.data
        res = error = None    
        collection_data = {"title":request_data.get("title"),
                            "description": request_data.get("description"),
                            "owner":self.user.id,
                            "updated_by":self.user.id}
        try:
            with transaction.atomic():
                
                if self.uu: 
                    collection_data['uuid'] = self.uu
                    instance = self.get_user_collections(self.uu)
                    instance = instance.first()
                    collection_serializer = MovieCollectionSerializer(instance,data = collection_data,partial=True) #update
                else: collection_serializer = MovieCollectionSerializer(data = collection_data) #create

                if collection_serializer.is_valid():
                    collection_serializer.save()
                    uu = collection_serializer.data['uuid']
                    if request_data.get('movies'): self.update_movie_in_collection(uu,self.bulk_create_movies(request_data.get('movies')))
                    res = collection_serializer.data['uuid']
                else: error = collection_serializer.errors 
        except Exception as e:
            print(e)
            error = str(e)

        return res,error

    def get(self):
        '''method to get collection list'''
        #todo favorites genres func
        res = error = {}
        try:
            collection_data = self.get_user_collections(self.uu)
            serializer = MovieCollectionSerializer(collection_data,context={'uu':self.uu}, many=True)   
            res['collections'] = serializer.data if serializer.data else "Empty Collection! please add New collections" 
            if collection_data and not self.uu: res['favourite_genres'] = self.get_favourite_genres(collection_data)
        except Exception as e:
            error = str(e)
        return res,error

    def delete(self):
        try:
            collection_data = self.get_user_collections(self.uu)
            if collection_data: collection_data.first().delete()
            else: return "Collection not found! Seems like its already deleted.",None
        except Exception as e:
            pass
        return True,None