from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup
import re

class Dom():
        url: str = None
        dom: str = None
        emails: set = None

        def __init__(self, url: str):
                self.url = url
                self.get_dom()
                self.list_email()

        def list_email(self):
                self.emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", self.dom))
                        
        def get_headings(self) -> ResultSet:
                soup = BeautifulSoup(self.dom, "lxml")
                headings = soup.find_all(re.compile('^h[1-6]$'))
                return headings

        def show_dom(self):
                print(self.dom)

        def get_dom(self):
                print(f"URL: {self.url}")
                http_obj = requests.get(self.url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'})
                self.dom = http_obj.text
        