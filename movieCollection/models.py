from django.db import models
from accounts.models import User
from movie.models import Movie
import uuid

# Create your models here.

class UserMovieCollection(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,unique=True)
    owner = models.ForeignKey(User,related_name='collections_owned',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500,null=True, blank=True)
    movies = models.ManyToManyField(Movie)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User,related_name='update_collections_owned', null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.title
    