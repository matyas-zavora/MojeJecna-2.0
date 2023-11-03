from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from response import Response
from _decorators.authDecoratos import AuthDecorators
from _decorators.requestFormating import RequestFormating
from rest_framework.views import APIView
from _methods.hash import sha256_hash

from dbModels.entities.authentication.user import User

import json

class UserDetailView(APIView):
    
    @RequestFormating.api_request_to_request
    @RequestFormating.api_GET_to_dictinary
    @AuthDecorators.check_hash()
    def get(self, request):
        try:
            query = request.GET
            print(query)
            users = User.objects.filter(**query)
            print(users)
            return Response.make_JSONresponse(200, content=[tmp.get_json() for tmp in users])
        except BaseException as e:
            print(type(e)," ==> ",e)
            return Response.make_JSONresponse(500)

    @RequestFormating.api_request_to_request
    @AuthDecorators.check_hash()
    @AuthDecorators.allowed_groups([])
    def post(self, request, format=None):
        try:
            raw_data = dict(request.POST)
            for mandatory_atribute in ['username', 'raw_password', 'email', 'first_name', 'last_name', 'user_type']:
                if not mandatory_atribute in raw_data:
                    return Response.make_JSONresponse(400, response_code='400_0002', atribute=mandatory_atribute)
            for optional_atribute in ['user_class', 'education_group', 'middle_name']:
                if not optional_atribute in raw_data:
                    raw_data[optional_atribute] = None
            processed_data = {}
            for key in raw_data:
                if raw_data[key] is None:
                    processed_data[key] = None
                    continue
                elif raw_data[key][0] == '':
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
            print(type(e)," ==> ",e)
            return Response.make_JSONresponse(500)
        
    def put(self, request):
        pass

    def delete(self, request):
        pass
    
@csrf_exempt
def POST_auth(request):
    try:
        if not request.method == 'POST':
            return Response.make_JSONresponse(405,atribute='method',content={'method': request.method})        
        
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        if not username:
            return Response.make_JSONresponse(400, response_code="400_0001", atribute='username')
        if not password:
            return Response.make_JSONresponse(400, response_code="400_0001", atribute='password')
        
        try:
            user: User = User.objects.get(username=username)
        except ObjectDoesNotExist:
            return Response.make_JSONresponse(400, atribute='username')

        print('správné heslo ==> ',user.password == sha256_hash(password))
        if not user.password == sha256_hash(password):
            return Response.make_JSONresponse(400, atribute='password')
        
        user_json = user.get_json()
        user_json["hash"] = user.make_auth_hash()
        #del user_json["password"]
        
        return Response.make_JSONresponse(200, None, content = user_json)
    except BaseException as e:
        return Response.make_JSONresponse(500)