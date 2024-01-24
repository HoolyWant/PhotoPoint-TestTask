from django.urls import path

from current.apps import CurrentConfig
from current.views import get_current

app_name = CurrentConfig.name

urlpatterns = [
    path('get-current-usd', get_current, name='get-current-usd'),
]
