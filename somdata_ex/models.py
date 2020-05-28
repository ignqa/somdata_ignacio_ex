from django.db import models


# Create your models here.
class BTCUSDT(models.Model):
    high = models.FloatField()
    low = models.FloatField()
    updated_at = models.DateTimeField()