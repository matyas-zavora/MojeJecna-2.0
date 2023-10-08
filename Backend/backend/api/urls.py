from django.urls import path
import api.authentication as auth

urlpatterns = [
    #Authentication
    path('login/', auth.login, name='api_auth_login')
]
