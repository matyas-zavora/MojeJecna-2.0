from django.http import JsonResponse

def login(request):
    print(request.GET.get('username'))
    print(request.GET.get('password'))
    return JsonResponse({"name": "Mates voní"}, status=200)