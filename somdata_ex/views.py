import requests
from django.shortcuts import render
from somdata_ex.models import BTCUSDT
from django.http import HttpResponse


# Create your views here.
def index(request):
    response = requests.get("https://api.bittrex.com/v3/markets/BTC-USDT/summary")
    if response.status_code == 200:
        r_json = response.json()
        point = BTCUSDT(high=r_json["high"], low=r_json["low"], updated_at=r_json["updatedAt"])

        point.save()

        return HttpResponse(response.json())