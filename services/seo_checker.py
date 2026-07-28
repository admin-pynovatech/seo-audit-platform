"""
SEO Analyzer

Responsible for extracting SEO-related information
from a BeautifulSoup object.
"""

from bs4 import BeautifulSoup


class SEOAnalyzer:
    """Extract SEO information from HTML."""

    def __init__(self, html: str):

        self.soup = BeautifulSoup(
            html,
            "html.parser"
        )

    # -------------------------------------------------
    # Title
    # -------------------------------------------------

    def get_title(self):

        if self.soup.title:
            return self.soup.title.get_text(strip=True)

        return "Not Found"

    # -------------------------------------------------
    # Meta Description
    # -------------------------------------------------

    def get_meta_description(self):

        meta = self.soup.find(
            "meta",
            attrs={"name": "description"}
        )

        if meta:
            return meta.get("content", "").strip()

        return "Not Found"

    # -------------------------------------------------
    # Headings
    # -------------------------------------------------

    def get_headings(self):

        headings = {}

        for tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:

            headings[tag.upper()] = [
                item.get_text(strip=True)
                for item in self.soup.find_all(tag)
            ]

        return headings

    # -------------------------------------------------
    # Analyze
    # -------------------------------------------------

    def analyze(self):

        return {

            "title": self.get_title(),

            "meta_description": self.get_meta_description(),

            "headings": self.get_headings(),

        }