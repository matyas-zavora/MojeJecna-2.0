from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from response import Response
from _decorators.authDecoratos import AuthDecorators
from rest_framework.views import APIView
from _methods.hash import sha256_hash

from dbModels.entities.authentication.user import User

class UserDetailView(APIView):
    
    def get(self, request):
        pass

    @AuthDecorators.check_hash()
    @AuthDecorators.allowed_groups([])
    def post(self, request):
        try:
            raw_data = dict(request.POST)

            for mandatory_atribute in ['username', 'raw_password', 'email', 'first_name', 'last_name', 'user_type_id']:
                if not mandatory_atribute in raw_data:
                    return Response.make_JSONresponse(400, response_code='400_0002', atribute=mandatory_atribute)
                
            for optional_atribute in ['user_class_id', 'education_group_id', 'middle_name']:
                if not optional_atribute in raw_data:
                    raw_data[optional_atribute] = None

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

            user = User.objects.create(**processed_data)

            user_json = user.get_json()
            user_json["hash"] = user.make_auth_hash()
            del user_json["password"]

            return Response.make_JSONresponse(201, content = user_json)
        except BaseException as e:
            return Response.make_JSONresponse(500)
        
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

        print(user.password)
        print(sha256_hash(password))
        print(not user.password == sha256_hash(password))
        if not user.password == sha256_hash(password):
            return Response.make_JSONresponse(400, atribute='password')
        
        user_json = user.get_json()
        user_json["hash"] = user.make_auth_hash()
        del user_json["password"]
        
        return Response.make_JSONresponse(200, None, content = user_json)
    except BaseException as e:
        return Response.make_JSONresponse(500)