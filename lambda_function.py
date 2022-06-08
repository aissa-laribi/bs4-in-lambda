import urllib.request
from bs4 import BeautifulSoup as soup
import time

def lambda_handler(event, context):
    urls = [
        'https://www.yellowpages.com/search?search_terms=fitness&geo_location_terms=New%20York%2C%20NY&page=1',
        'https://www.yellowpages.com/search?search_terms=fitness&geo_location_terms=New%20York%2C%20NY&page=2',
        'https://www.yellowpages.com/search?search_terms=fitness&geo_location_terms=New%20York%2C%20NY&page=3',
        'https://www.yellowpages.com/search?search_terms=fitness&geo_location_terms=New%20York%2C%20NY&page=4',
        
    ]
    for url in urls:
        headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        page_html = response.read()
        time.sleep(5)
        page_soup = soup(page_html, "html.parser")
        for link in page_soup.find_all('a', class_= "track-visit-website",):
            print(link.get('href', "a"))
