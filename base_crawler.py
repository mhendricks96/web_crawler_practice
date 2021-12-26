import requests
from bs4 import BeautifulSoup


def get_links_on_page(url):
  links = []
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'lxml')
  section = soup.find('section', {'id':'mainaside'})
  for link in section.findAll(('a')):
    href = link.get('href')
    if 'guatemala' in href:
      # print('saved',href)
      links.append(href)
  return links


def get_article_links(beginURL):
  links = []
  max_pages = 5
  current_page = 0
  next_page = 1
  links.extend(get_links_on_page(beginURL))
  # get_links_on_page(startURL)
  # print(startURL)

  while current_page < max_pages:
    # print(beginURL)
    new_link = f'{beginURL}?page={str(next_page)}'
    if new_link:
      current_page += 1
      next_page += 1
      links.extend(get_links_on_page(new_link))
      # currentUrl = new_link
      # startUrl = new_link
  
  for link in links:
    print(link)




get_article_links('https://www.infoplease.com/search/guatemala')