import requests

from datetime import date, timedelta
from pprint import pprint

def get_rates(currencies, days=30):
    end_date = date.today()
    delta = timedelta(days=days)
    start_date = end_date - delta
    url = requests.get(f'http://api.exchangerate.host/timeseries?start_date={start_date}&end_date={end_date}&symbols={",".join(currencies)}')
    if not url and url.json():
        return False,False
    api_rate = url.json().get("rates")
    #pprint(api_rate)
    all_day = sorted(api_rate.keys())
    all_rates = { currency : [] for currency in currencies }

    for day in all_day :
        [all_rates[currency].append(rate) for currency, rate in api_rate[day].items()]
    return all_day, all_rates

if __name__ == "__main__":
    pprint(get_rates(currencies=["USD","CAD"]))

