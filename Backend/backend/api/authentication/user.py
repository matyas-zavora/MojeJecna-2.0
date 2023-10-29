from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from response import Response
from _decorators.apiAuth import check_auth, check_hash
from rest_framework.views import APIView
from _methods.hash import sha256_hash

from dbModels.entities.authentication.user import User

class UserDetailView(APIView):
    
    def get(self, request):
        pass

    def post(self, request):
        raw_data = dict(request.POST)
        
        for mandatory_atribute in []:
            return Response.make_JSONresponse(400)
        
        processed_data = {}
        for key in raw_data:
            if raw_data[key][0] == '':
                processed_data[key] = None
                continue
            elif raw_data[key][0].isdigit():
                processed_data[key] = int(raw_data[key][0])
                continue
            processed_data[key] = raw_data[key][0]
        
        processed_data['password'] = sha256_hash(processed_data.pop('raw_password'))
        
        print(processed_data)
        
        user = User.objects.create(**processed_data)
        
        return Response.make_JSONresponse(201, content = user.get_json())

    def put(self, request):
        pass

    def delete(self, request):
        pass
    
def get_auth(request):
    try:
        username = request.GET.get('username', None)
        password = request.GET.get('password', None)
        
        if not username:
            return Response.make_JSONresponse(400, response_code="400_0001", atribute='username')
        if not password:
            return Response.make_JSONresponse(400, response_code="400_0001", atribute='password')
        
        try:
            user: User = User.objects.get(username=username)
        except ObjectDoesNotExist:
            return Response.make_JSONresponse(400, atribute='username')

        if not user.password == password:
            return Response.make_JSONresponse(400, atribute='password')
        
        return Response.make_JSONresponse(200, None, content = user.get_json())
    except BaseException as e:
        print(type(e), "==>",e)
        return Response.make_JSONresponse(500)