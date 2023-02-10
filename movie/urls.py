from django.urls import path
from movie.views import *

urlpatterns = [
    path('', MovieApiView.as_view(), name='movies'),
]