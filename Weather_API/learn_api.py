import requests
import urllib
import re


def get_quote():
    response = requests.get("https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    quote = data['quote']
    print(quote)


def sunrise_data():
    response = requests.get("https://api.sunrise-sunset.org/json")
    if re.search(r'[2][0-9]{2}',str(response.status_code)):
        print("passed")
        data = response.json()


sunrise_data()


