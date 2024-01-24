import json

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from current.models import UserRequest
from current.services import get_currency


class GetCurrent(ListView):
    model = UserRequest

    def get(self, request, *args, **kwargs):
        queryset = UserRequest.objects.all().order_by('pk')[:11]
        response = get_currency()
        currency = UserRequest.objects.create(currency=response)
        json_queryset = serializers.serialize('json', queryset)
        return HttpResponse(json_queryset, content_type='application/json')

