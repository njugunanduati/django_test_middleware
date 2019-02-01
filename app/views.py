import json
from django.http import JsonResponse
from datetime import date


def get_api(request):
    status_code = 200
    result = {"status": status_code, "message": "the api is being cached"}
    return JsonResponse(result)
