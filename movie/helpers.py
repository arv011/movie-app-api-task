import requests
from requests.auth import HTTPBasicAuth
import json
from django.conf import settings
from movie.models import GENRE_CHOICES

def get_movies_credy_api(url= None,page=None):
    '''get movies list from credy api applied reapply call machanism till 10 times'''
    # {"is_success":false,"error":{"message":"database connection failed.","code":"service_error"}}

    status, count, response = False, 0 , None
    url = url if url else 'https://demo.credy.in/api/v1/maya/movies/' 
    if page: url = url + '?page=' + page

    while not status and count != 10:
        res = requests.get(url, auth=HTTPBasicAuth(settings.CREDY_USERNAME, settings.CREDY_PASSWORD))
        res = json.loads(res.content)
        if res.get('count',0) > 0: status, response = True, res
        else: count += 1
    return response
    