import urllib.request
import re
import time
from bs4 import BeautifulSoup
from dy.models import DyModels
def crawl(url):
    page = urllib.request.urlopen(url)
    contents = page.read()
    soup = BeautifulSoup(contents)
    for tag in soup.find_all('div', class_='item'):
        m_order=tag.em.get_text()
        m_name=tag.span.get_text()
        m_url=str(tag.find('a')).split('"')[1]
        dymodels=DyModels(title=m_name,content=0, link=m_url)
        dymodels.save()
def savedata():
    for n in range(0,250,25):
        crawl(f"https://movie.douban.com/top250?start={n}&filter=")

