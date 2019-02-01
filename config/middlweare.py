from django.utils.deprecation import MiddlewareMixin
from django.http import Http404
from config.settings import CACHE_URLS


class CacheMiddleware(MiddlewareMixin):

    """
    A middleware class to cache the url based on the time
    """
    def process_request(self, request):
        allowed_urls = CACHE_URLS
        ip = request.META.get('REMOTE_ADDR')
        if ip not in allowed_urls:
            raise Http404
        return None
