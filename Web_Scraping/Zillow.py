import requests
import json
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
