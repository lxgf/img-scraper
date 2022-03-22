from xml.etree.ElementTree import tostring
import requests
from bs4 import BeautifulSoup

url = 'https://slackmojis.com/'
page_response = requests.get(url)
soup = BeautifulSoup(page_response.text, 'lxml')
quotes = soup.find_all('img')

for idx, quote in enumerate(quotes):
    img_url = quote['src']
    if img_url[0:2] == '//':
        img_url = 'https://' + img_url[2:len(img_url)]
    img_response = requests.get(img_url)
    if img_response.status_code == 200:
        with open('data/' + str(idx) + '.gif','wb') as imgfile:
            imgfile.write(img_response.content)