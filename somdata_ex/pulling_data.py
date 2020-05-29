import requests
from somdata_ex.models import BTCUSDT

_DATA_SOURCE = "https://api.bittrex.com/v3/markets/BTC-USDT/summary"


def pull():
    response = requests.get(_DATA_SOURCE)
    if response.status_code == 200:
        r_json = response.json()
        point = BTCUSDT(high=r_json["high"], low=r_json["low"], updated_at=r_json["updatedAt"])
        point.save()
