from django.core.cache import cache
from config.settings import CACHE_URLS
from app.utils import get_random_digits


class CacheMiddleware:
    """
    A middleware class to cache the url based on the time
    """
    def process_request(self, request, duration):
        rand_key = int(get_random_digits(7))
        allowed_urls = CACHE_URLS
        absolute_root = request.build_absolute_uri('/').strip("/")
        get_endpoint = request.build_absolute_uri().strip(absolute_root)+'0/'
        get_endpoint = "/"+get_endpoint
        if get_endpoint in allowed_urls:
            cache_key = '{}_my_key_{}'.format(rand_key, duration)
            cache_time = int(duration) * int(duration)
            data = cache.get(cache_key)
            cache.set(cache_key, data, cache_time)
            return cache
        return None
