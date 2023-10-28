from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from response import Response
from _decorators.apiAuth import check_auth, check_hash
from rest_framework.views import APIView

from dbModels.entities.authentication.user import User

class UserDetailView(APIView):
    
    def get(self, request):
        try:
            username = request.query_params.get('username', None)
            password = request.query_params.get('password', None)
            
            try:
                user: User = User.objects.get(username=username)
            except ObjectDoesNotExist:
                return Response.make_JSONresponse(400, atribute='username')

            if not user.password == password:
                return Response.make_JSONresponse(400, atribute='password')
            
            return Response.make_JSONresponse(200, None, content = user.get_json())
        except BaseException as e:
            print(type(e))
            return Response.make_JSONresponse(500)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass