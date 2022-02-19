import json
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import time

def lambda_handler(event, context):
    urls = [
    'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=631915792&keywords=fitness&location=london&pageNum=1',
    'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=631915792&keywords=fitness&location=london&pageNum=2',
    'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=631915792&keywords=fitness&location=london&pageNum=3',
    'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=631915792&keywords=fitness&location=london&pageNum=4',
    'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=631915792&keywords=fitness&location=london&pageNum=5',
    'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=631915792&keywords=fitness&location=london&pageNum=6',
    'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=631915792&keywords=fitness&location=london&pageNum=7',
    'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=631915792&keywords=fitness&location=london&pageNum=8',
    'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=631915792&keywords=fitness&location=london&pageNum=9',
    'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=631915792&keywords=fitness&location=london&pageNum=10',

    ]
    for url in urls:
        headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        page_html = response.read()
        time.sleep(10)
        page_soup = soup(page_html, "html.parser")
        for link in page_soup.find_all('a', class_= "btn btn-yellow businessCapsule--ctaItem",):
            print(link.get('href', "a"))