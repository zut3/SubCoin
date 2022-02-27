from .models import Price
from requests import get

supported = {
    "eth": 'Ethereum',
    "btc": "Bitcoin",
}


def set_data():
    val = supported.keys()
    Price.objects.all().delete()

    for item in val:
        g = item + "_usd"
        url = f"https://yobit.net/api/3/ticker/{g}"
        res = get(url).json()
        avg = round(res[g]["avg"], 2)
        new = Price(name=supported[item], price=avg)
        new.save()

