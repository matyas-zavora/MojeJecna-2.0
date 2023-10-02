from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    print(request.method)
    print('headers:')
    print('-')
    for param in request.headers:
        print(param,' ==> ',request.headers[param])
    print('query:')
    print('-')
    for param in request.GET:
        print(param,' ==> ',request.GET[param])
    return JsonResponse({
        "name":"pp"
    })