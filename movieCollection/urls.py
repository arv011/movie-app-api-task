from django.urls import path
from movieCollection.views import *

urlpatterns = [
    path('', MovieCollectionApiView.as_view(), name='movie_collections'),
    path('<uuid:uuid>', MovieCollectionApiView.as_view(), name='collection'),
]