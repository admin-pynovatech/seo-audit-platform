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

            href = tag.get("href", "").strip()

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

    def check_link_status(self, url):

        try:

            response = requests.get(
                url,
                timeout=10,
                allow_redirects=True,
                headers={
                    "User-Agent": "Mozilla/5.0"
                }
            )

            return response.status_code

        except requests.RequestException:

            return None

    def find_broken_links(self):

        broken_links = []

        categorized = self.categorize_links()

        all_links = (
            categorized["internal"] +
            categorized["external"]
        )

        for link in all_links:

            status = self.check_link_status(link)

            if status is None or status >= 400:

                broken_links.append({
                    "url": link,
                    "status": status
                })

        return broken_links

    def get_summary(self):

        categorized = self.categorize_links()

        broken_links = self.find_broken_links()

        total_links = (
            len(categorized["internal"]) +
            len(categorized["external"])
        )

        return {

            "total_links": total_links,

            "internal_links": len(
                categorized["internal"]
            ),

            "external_links": len(
                categorized["external"]
            ),

            "broken_links": len(
                broken_links
            ),

            "details": broken_links
        }