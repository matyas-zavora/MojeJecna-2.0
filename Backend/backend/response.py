from json import JSONEncoder
from django.http import JsonResponse
from typing import Any, Union
            
class Response:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def __make_status(code: int) -> str:
        tmp: str = str(code)
        if tmp[0] == '2':
            return 'OK'
        elif tmp[0] == '4':
            return 'ER'
        
    @staticmethod
    def make_JSONresponse(code: int, content: Union[dict, None] = None, **kwargs: dict) -> JsonResponse:
        meta: dict = {
            "status": Response.__make_status(code),
            "code": code,
            "atribute": kwargs.pop('stribute', None),
            "status_code": kwargs.pop('status_code', None)
        }
        request_parameters: dict = {
            "body": kwargs.pop('body_params', None),
            "query": kwargs.pop('query_params', None),
            "path": kwargs.pop('path_params', None)
        }
        response_content={
            "meta":meta,
            "parameters": request_parameters
        }
        if not content == None:
            if isinstance(content, list):
                response_content["count"] = len(content)
            response_content["content"] = content
        return JsonResponse(response_content, status=code)