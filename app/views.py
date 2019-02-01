import json
from django.http import JsonResponse
from app.utils import get_random_digits
from config.middlweare import CacheMiddleware


def get_api(request, **kwargs):
    duration = kwargs['duration']
    middleware = CacheMiddleware()
    try:
        cache = middleware.process_request(request, duration)
        status_code = 200
        result = {"status": status_code, "message": "the api is being cached"}
    except Exception as e:
        status_code = 404
        result = {"status": status_code, "message": str(e)}
    return JsonResponse(result)
