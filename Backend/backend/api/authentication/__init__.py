from django.http import JsonResponse, HttpResponse
from response import Response
from _decorators.apiAuth import check_auth, check_hash



@check_auth()
def login(request):
    return HttpResponse("<h1>ahojky</h1>")
