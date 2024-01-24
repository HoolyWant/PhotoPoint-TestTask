from django.urls import path

from current.apps import CurrentConfig
from current.views import GetCurrent

app_name = CurrentConfig.name

urlpatterns = [
    path('get-current-usd', GetCurrent.as_view(), name='get-current-usd'),
]
