import requests
from bs4 import BeautifulSoup
import time


def get_links_on_page(url):
  '''returns a list of all the relevant links on a given page'''
  links = []
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'lxml')
  section = soup.find('section', {'id':'mainaside'})
  for link in section.findAll(('a')):
    href = link.get('href')
    if 'christmas' in href:
      links.append(href)
  return links


def get_title_from_article(link):
  '''function takes in a link and returns the headline on that links page'''
  page = requests.get(link).text
  soup = BeautifulSoup(page, 'lxml')
  article = soup.find('article', {'class': 'col-sm-8'})
  title = article.find(('h1')).text
  print(title)
  return title

def get_article_links(beginURL):
  links = set()
  max_pages = 1
  current_page = 0
  next_page = 1
  link_info = {}
  for link in get_links_on_page(beginURL):
    links.add(link)

  while current_page < max_pages:
    new_link = f'{beginURL}?page={str(next_page)}'
    if new_link:
      current_page += 1
      next_page += 1
      for link in get_links_on_page(new_link):
        links.add(link)
  
  for link in links:
    time.sleep(2)
    title = get_title_from_article(f'https://www.infoplease.com{link}')
    link_info[f'https://www.infoplease.com{link}'] = title
    
  for value in link_info.values():
    print(value)
  
  



get_article_links('https://www.infoplease.com/search/christmas')

