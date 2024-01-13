import requests
import json
from bs4 import BeautifulSoup
import lxml

headers = {'Accept-Encoding': 'identity'}
response = requests.get("https://www.python.org", headers=headers)
# print(type(response.content))
# print(response.content.decode("utf8"))
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

anchor_tags = soup.find_all(name = 'a')
# p_tags = soup.find_all(name = 'p')

# for tag in anchor_tags:
#     # print(tag.getText())
#     print(tag.get('href'))

url_specific_css = soup.select_one(selector="p a")
url_specific_css = soup.select(selector="p a")
print(url_specific_css)



