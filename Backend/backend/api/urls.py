from django.urls import path
from api.authentication.user import UserDetailView, POST_auth

urlpatterns = [
    #Authentication
    path('auth/user/', POST_auth),
    path('user/', UserDetailView.as_view()),
    
    #path('auth/group/', , name=''),
    #path('auth/mnUserGroup/', , name=''),
]