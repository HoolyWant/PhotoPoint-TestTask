from django.db import models


class UserRequest(models.Model):
    usd_to_rub = models.FloatField(verbose_name='курс доллара к рублю')
