from urllib.request import urlopen  as uReq
from bs4 import BeautifulSoup as soup

MyUrl = "https://twitter.com"

#scrapping
uClient = uReq(MyUrl)

PageHtml = uClient.read()

uClient.close()

PageSoup = soup(PageHtml, "html.parser")