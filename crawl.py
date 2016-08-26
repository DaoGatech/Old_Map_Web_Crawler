import urllib.request
import json
import re
from bs4 import BeautifulSoup
import lxml
import CONFIG


def crawl():
    web = urllib.request.urlopen(CONFIG.CRAWL_MAIN_LINK)
    soup = BeautifulSoup(web.read(), 'lxml')
    pages = soup.findAll('div', {'class': 'pages'})
    last_page = pages[0].findAll('a')[8].contents[0]

    for i in range(1,int(last_page)):
        print(i)
        
    photo_ids = []
    for script in soup.find_all('script', {'src': False}):
        if script:
            values = re.findall(r'var photo_ids =\s*(.*?);', script.string, re.DOTALL | re.MULTILINE)
            if len(values) > 0:
                photo_ids = values
                break

    photo_ids = json.loads(photo_ids[0])
    for photo in photo_ids:
        web = urllib.request.urlopen(CONFIG.PHOTO_LINK + photo)
        soup = BeautifulSoup(web.read(), 'lxml')
        mydivs = soup.findAll('div', {'class': 'stylelistrow'})

crawl()
