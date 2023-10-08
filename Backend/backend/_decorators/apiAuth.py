from django.http import JsonResponse

def check_auth():
    """
        Dekorátor, který zkontroluje jestli v headeru requestu jsou atributy
        - user_hash
        - user_id


    """
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            atributes = [
            request.headers.get('user_id',None),
            request.headers.get('user_hash',None)
            ]
            if None in atributes:
                return JsonResponse({}, status=404)
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator

def check_hash():
    pass