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
    last_page = pages[0].findAll('a')[len(pages[0].findAll('a')) - 2].contents[0]
    for i in range(1, int(last_page)):
        web = urllib.request.urlopen(CONFIG.CRAWL_MAIN_LINK_WITH_PAGE + str(i))
        soup = BeautifulSoup(web.read(), 'lxml')
        photo_ids = []
        for script in soup.find_all('script', {'src': False}):
            if script:
                values = re.findall(r'var photo_ids =\s*(.*?);', script.string, re.DOTALL | re.MULTILINE)
                if len(values) > 0:
                    photo_ids = values
                    break
        photo_ids = json.loads(photo_ids[0])
        for photo in photo_ids:
            web = urllib.request.urlopen(CONFIG.PHOTO_LINK + str(photo))
            soup = BeautifulSoup(web.read(), 'lxml')
            latitude = soup.findAll('abbr', {'class': 'latitude'})
            longitude = soup.findAll('abbr', {'class': 'longitude'})
            print(latitude[0]['title'])
            print(longitude[0]['title'])

crawl()
