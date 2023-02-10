from django.urls import path
from accounts.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# app_name = "accounts"

urlpatterns = [
    path('', FirstPage.as_view(), name='firstpage'),
    path('register/',RegiterApiView.as_view(),name='register'),
    path('login/',LoginApiView.as_view(),name='login'),
    path('token/',TokenObtainPairView.as_view(),name='token'),
    path('token/refresh/',TokenRefreshView.as_view(),name='refresh-token'),
    path('request-count/',RequestCounterApiView.as_view(),name='request-count'),
    path('request-count/reset/',RequestCounterResetApiView.as_view(),name='request-count-reset')

    # path('api/password/change/', ChangePasswordView.as_view(), name='change-password'),
]

