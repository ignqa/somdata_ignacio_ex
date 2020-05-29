from django.db import models


class BTCUSDT(models.Model):
    high = models.FloatField()
    low = models.FloatField()
    updated_at = models.DateTimeField()
