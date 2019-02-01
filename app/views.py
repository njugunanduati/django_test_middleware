import json
from django.http import JsonResponse
from django.core.cache import cache
from app.utils import get_random_digits


def get_api(request, **kwargs):
    rand_key = int(get_random_digits(7))
    duration = kwargs['duration']
    cache_key = '{}_my_key_{}'.format(rand_key, duration)
    cache_time = int(duration) * int(duration)
    data = cache.get(cache_key)
    cache.set(cache_key, data, cache_time)
    try:
        if cache:
            status_code = 200
            result = {"status": status_code, "message": "the api is being cached for {} minutes".format(cache_time)}
    except:
        status_code = 404
        result = {"status": status_code, "message": "Error!"}
    return JsonResponse(result)
