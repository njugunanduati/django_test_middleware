
from django.conf.urls import url
from app.views import get_api


urlpatterns = [
    url(r'^test/(?P<duration>\w{0,50})/$', get_api,),
]
