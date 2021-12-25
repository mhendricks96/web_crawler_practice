import requests
from bs4 import BeautifulSoup


# startUrl = 'https://www.infoplease.com/search/guatemala'
# links = []

def get_article_links(startURL):
  links = []
  max_pages = 1
  current_page = 0

  def get_links_on_page(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    section = soup.find('section', {'id':'mainaside'})
    for link in section.findAll(('a')):
      href = link.get('href')
      if 'guatemala' in href:
        print('saved',href)
        links.append(href)

  def find_next_page():
    next_page = soup.find('li', {'class':'pager__item page__item--next'}).find('a').get('href')
    
    if next_page:
      return next_page
    else:
      return False

  
  get_links_on_page(startURL)

  if current_page < max_pages:
    new_link = find_next_page()
    if new_link:
      current_page += 1
      get_links_on_page(startUrl + new_link)
  
  for link in links:
    print(link)




get_article_links('https://www.infoplease.com/search/guatemala')