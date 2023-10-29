from django.http import JsonResponse
from response import Response

def check_auth():
    """
        Dekorátor, který zkontroluje jestli v headeru requestu jsou atributy
        - user_hash
        - user_id


    """
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
    pass

def allowed_groups(groups=[]):
    pass