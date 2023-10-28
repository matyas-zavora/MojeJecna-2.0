from django.urls import path
from api.authentication.user import UserDetailView

urlpatterns = [
    #Authentication
    path('auth/user/', UserDetailView.as_view(), name='api_auth_login'),
    #path('auth/group/', , name=''),
    #path('auth/mnUserGroup/', , name=''),
]