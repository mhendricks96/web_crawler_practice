import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.infoplease.com/search/guatemala')

# lxml is the method of extraction
soup = BeautifulSoup(page.text, 'lxml')