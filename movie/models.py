from django.db import models
from accounts.models import User
import uuid
from multiselectfield import MultiSelectField

# Create your models here.
GENRE_CHOICES = {
    ('Action','Action'),
    ("Drama","Drama"),
    ("Thriller","Thriller"), 
    ("Horror","Horror"),
    ("Mystery","Mystery"), 
    ("Science Fiction","Science Fiction"),
    ("Romance","Romance"),
    ("Family","Family"),
    ("Comedy","Comedy"),
    ("Crime","Crime"),
    ("Documentary","Documentary"),
}   


class Movie(models.Model):
    '''Movies stores belongs from collection'''
    uuid = models.UUIDField(default=uuid.uuid4,editable=True,unique=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500,null=True, blank=True)
    genres = MultiSelectField(choices = GENRE_CHOICES, max_choices=10,max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField(null=True,blank=True)
    updated_by = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.title
    


