

def check_auth(view_func):
    """
    Dekorátor, který zkontroluje jestli v headeru requestu jsou atributy
    - hash
    - user_id
    
    
    """
    def wrapper_func(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)

    return wrapper_func

def check_hash():
    pass
