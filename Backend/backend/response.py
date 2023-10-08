from django.http import JsonResponse

class Response:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def make_response(status=None):
        return ''