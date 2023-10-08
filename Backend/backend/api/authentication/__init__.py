from django.http import JsonResponse
from _decorators.apiAuth import check_auth, check_hash

@check_auth()
def login(request):
    print(request.GET.get('username'))
    print(request.GET.get('password'))
    return JsonResponse({"name": "Mates voní"}, status=200)
