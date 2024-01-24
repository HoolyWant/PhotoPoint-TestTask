import time

from django.core import serializers
from django.http import HttpResponse
from django_ratelimit.decorators import ratelimit

from current.models import UserRequest
from current.services import get_currency


def get_current(request):
    time.sleep(10)
    queryset = UserRequest.objects.all().order_by('-pk')[:10]
    response = get_currency()
    UserRequest.objects.create(usd_to_rub=response)
    json_queryset = serializers.serialize('json', queryset)
    return HttpResponse(json_queryset, content_type='application/json')


