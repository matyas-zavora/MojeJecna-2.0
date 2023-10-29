from django.http import JsonResponse
from typing import Union

class Response:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def make_meta(code: int, response_code: int, atribute: str) -> dict:
        tmp: str = str(code)
        status: str = None
        if tmp[0] in ['4','5']:
            status = 'ER'
        elif tmp[0] == '2':
            status = 'OK'
        elif tmp[0] == '3':
            status = 'RE'
        return {
            "status": status,
            "code": code,
            "response_code": response_code,
            "atribute": atribute
        }
        
    
    @staticmethod
    def make_JSONresponse(code: int, response_code: int=None, atribute: str=None, content: Union[dict, list] = None, **kwargs) -> JsonResponse:
        response: dict={
            "meta":Response.make_meta(code, response_code = response_code, atribute = atribute)
        }
        response.update(kwargs)
        if response["meta"]["status"] == "OK":
            if type(content) == list:
                response["count"] = len(content)
            response["content"]=content
        return JsonResponse(response, status=code)