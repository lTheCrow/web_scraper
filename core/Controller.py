from core.Dom import Dom
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class Controller():
        url: str = None
        dom: Dom = None

        def set_dom_url(self):
                self.dom = Dom(self.url)

        def get_email_list(self) -> set:
                return self.dom.emails

        def save_headings(self):
                headings = self.dom.get_headings()
                f = open(f"{urlparse(self.url).netloc}.txt", "a+")
                f.write("Heading List:\n")
                for heading in headings:
                        soup = BeautifulSoup(str(heading), "lxml")
                        f.write("\t" + soup.text + "\n")
                f.close()

        def save_email_list(self):
                if len(self.dom.emails) > 0:
                        f = open(f"{urlparse(self.url).netloc}.txt", "w+")
                        f.write("Email List:\n")
                        for email in self.dom.emails:
                                f.write("\t" + email + "\n")
                        f.close()