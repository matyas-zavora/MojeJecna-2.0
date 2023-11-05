from json import JSONEncoder
from typing import Any, Union, List
from django.http import JsonResponse
from response import Response
from _methods.hash import sha256_hash
from dbModels.entities.authentication.user import User
from dbModels.entities.authentication.mnUserGroup import MnUserGroup

class AuthDecorators:
    
    @staticmethod
    def __check_hash(user_id: int, user_hash: str) -> Union[JsonResponse, None]:
        if user_id is None:
            return Response.make_JSONresponse(
                401,
                response_code='',
                atribute='User-Id'
            )
        elif user_hash is None:
            return Response.make_JSONresponse(
                401,
                response_code='',
                atribute='User-Hash'
            )
        user: User = User.objects.get(id=user_id)
        if not user_hash == user.make_auth_hash():
            return Response.make_JSONresponse(
                401,
                response_code='',
                atribute='User-Hash'
            )

    @staticmethod
    def check_auth():
        def decorator(view_func):
            def wrapper_func(request, *args, **kwargs):
                atributes = [
                request.headers.get('User-Id',None),
                request.headers.get('User-Hash',None)
                ]
                if None in atributes:
                    queries: dict = dict(request.GET)
                    return Response.make_JSONresponse(
                        401,
                        response_code=''
                    )
                return view_func(request, *args, **kwargs)
            return wrapper_func
        return decorator
    
    @staticmethod
    def check_hash():
        def decorator(view_func):
            def wrapper_func(request, *args, **kwargs):
                user_id = request.headers.get('User-Id',None)
                user_hash = request.headers.get('User-Hash',None)
                if user_id is None:
                    return Response.make_JSONresponse(
                        401,
                        response_code='',
                        atribute='User-Id'
                    )
                elif user_hash is None:
                    return Response.make_JSONresponse(
                        401,
                        response_code='',
                        atribute='User-Hash'
                    )
                user: User = User.objects.get(id=user_id)
                if not user_hash == user.make_auth_hash():
                    return Response.make_JSONresponse(
                        401,
                        response_code='',
                        atribute='User-Hash'
                    )
                return view_func(request, *args, **kwargs)
            return wrapper_func
        return decorator
    
    @staticmethod
    def allowed_groups(group_codes=[]):
        def decorator(view_func):
            def wrapper_func(request, *args, **kwargs):
                user_id = request.headers.get('User-Id',None)
                user_hash = request.headers.get('User-Hash',None)
                
                user_groups_codes = MnUserGroup.objects.filter(user__id=user_id).values_list('group__code', flat=True)
                
                if not len(group_codes) == 0 and not any(user_groups_codes, group_codes):
                    return Response.make_JSONresponse(401)
                                    
                return view_func(request, *args, **kwargs)
            return wrapper_func
        return decorator
    
    @staticmethod
    def check_hash_and_permissions(group_codes: Union[List[str], str] = '*'):
        def decorator(view_func):
            def wrapper_func(request, *args, **kwargs):
                user_id = request.headers.get('User-Id',None)
                user_hash = request.headers.get('User-Hash',None)
                check_hash_result = AuthDecorators.__check_hash()
                if not check_hash_result is None:
                    return check_hash_result
                
                user_groups_codes = MnUserGroup.objects.filter(user__id=user_id).values_list('group__code', flat=True)
                if not group_codes == '*' and not any(user_groups_codes, group_codes):
                    return Response.make_JSONresponse(401)
                
                return view_func(request, *args, **kwargs)
            return wrapper_func
        return decorator
        