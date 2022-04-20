from requests import get
from bs4 import BeautifulSoup
from urllib.parse import quote

def Search(query : str = None):
    try:
        src = BeautifulSoup(get("https://www.google.com/search?q={}&num=100&hl=en".format(quote(query)), headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"}).text, "html.parser")
        return dict(title = src.find("h3", attrs={"class" :"LC20lb MBeuO DKV0Md"}).text, url = src.find("div", attrs={"class" : "yuRUbf"}).find("a").get("href"))
    except AttributeError as err : dict(message = "No Result Found!")