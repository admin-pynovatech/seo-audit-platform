import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


class BrokenLinkChecker:
    def __init__(self, url: str, html: str):
        self.url = url
        self.soup = BeautifulSoup(html, "html.parser")

    def extract_links(self):
        links = set()
        for tag in self.soup.find_all("a", href=True):
            href = tag.get("href").strip()
            if not href:
                continue
            absolute_url = urljoin(self.url, href)
            links.add(absolute_url)
        return list(links)

    def categorize_links(self):
        internal = []
        external = []
        base_domain = urlparse(self.url).netloc

        for link in self.extract_links():
            domain = urlparse(link).netloc
            if domain == base_domain:
                internal.append(link)
            else:
                external.append(link)
        return {
            "internal": internal,
            "external": external
        }