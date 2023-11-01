class RequestFormating:
    
    @staticmethod
    def api_request_to_request(view_func):
        def wrapper_func(request, *args, **kwargs):
            request=request.request
            return view_func(request, *args, **kwargs)
        return wrapper_func
    
    @staticmethod
    def api_GET_to_dictinary(view_func):
        def wrapper_func(request, *args, **kwargs):
            query = request.GET
            request.GET = {key:query[key] for key in query}
            return view_func(request, *args, **kwargs)
        return wrapper_func