from django.http import JsonResponse
from response import Response
from _methods.hash import sha256_hash
from dbModels.entities.authentication.user import User

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
                    response_code='',
                    **request.GET.dict()
                )
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator

def check_hash():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            user_id = request.headers.get('User-Id',None),
            user_hash = request.headers.get('User-Hash',None)
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

def allowed_groups(group_codes=[]):
    pass