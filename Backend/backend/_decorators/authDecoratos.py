from django.http import JsonResponse
from response import Response
from _methods.hash import sha256_hash
from dbModels.entities.authentication.user import User

class AuthDecorators:

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
                user_id = request.headers.get('User-Id',None),
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
                return view_func(request, *args, **kwargs)
            return wrapper_func
        return decorator