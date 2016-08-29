import urllib.request
import json
import re
from bs4 import BeautifulSoup
import lxml
import CONFIG
import database


def crawl():
    # Crawl the page to figure out how many pages of images
    web = urllib.request.urlopen(CONFIG.CRAWL_MAIN_LINK)
    soup = BeautifulSoup(web.read(), 'lxml')
    pages = soup.findAll('div', {'class': 'pages'})
    last_page = pages[0].findAll('a')[len(pages[0].findAll('a')) - 2].contents[0]

    # Crawl all the data of images in each page and figure list of photo ids
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

        # Return the data of each image based on its photo id
        photo_ids = json.loads(photo_ids[0])
        for photo in photo_ids:
            web = urllib.request.urlopen(CONFIG.PHOTO_LINK + str(photo))
            soup = BeautifulSoup(web.read(), 'lxml')
            latitude = soup.findAll('abbr', {'class': 'latitude'})
            longitude = soup.findAll('abbr', {'class': 'longitude'})
            img_title = soup.findAll('h1', {'id': 'photo-title'})[0].contents[0].strip()
            latitude = latitude[0]['title']
            longitude = longitude[0]['title']
            img_url = CONFIG.IMG_SRC + str(photo) + '.jpg'
            # Store the data into the database
            database.insert_to_database(img_title, latitude, longitude, img_url)
            print(str(photo) + ' = Success!')
crawl()
