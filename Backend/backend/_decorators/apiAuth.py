from django.http import JsonResponse

def check_auth(view_func):
    """
    Dekorátor, který zkontroluje jestli v headeru requestu jsou atributy
    - user_hash
    - user_id
    
    
    """
    def wrapper_func(request, *args, **kwargs):
        atributes = [
        request.headers.get('user_id',None),
        request.headers.get('user_hash',None)
        ]
        if None in atributes:
            return JsonResponse({}, code=404)
        return view_func(request, *args, **kwargs)
    return wrapper_func

def check_hash():
    pass