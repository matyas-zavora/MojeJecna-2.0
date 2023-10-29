from django.urls import path
from api.authentication.user import UserDetailView, get_auth

urlpatterns = [
    #Authentication
    path('auth/user/', get_auth, name = ''),
    path('user/', UserDetailView.as_view(), name = 'api_auth_login'),
    
    #path('auth/group/', , name=''),
    #path('auth/mnUserGroup/', , name=''),
]