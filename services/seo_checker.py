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

        "title_analysis": self.evaluate_title(),
        "meta_analysis": self.evaluate_meta_description(),
        "h1_analysis": self.evaluate_h1(),
        }

    # -------------------------------------------------
    # Title Evaluation
    # -------------------------------------------------

    def evaluate_title(self):

        title = self.get_title()

        if title == "Not Found":
            return {
                "value": title,
                "status": "Fail",
                "score": 0,
                "message": "Title tag is missing."
            }

        length = len(title)

        if 50 <= length <= 60:
            status = "Pass"
            score = 10
            message = "Title length is optimal."
        elif 30 <= length < 50 or 60 < length <= 70:
            status = "Warning"
            score = 7
            message = "Title length could be improved."
        else:
            status = "Fail"
            score = 3
            message = "Title is too short or too long."

        return {
            "value": title,
            "length": length,
            "status": status,
            "score": score,
            "message": message,
        }

    # -------------------------------------------------
    # Meta Description Evaluation
    # -------------------------------------------------

    def evaluate_meta_description(self):
        description = self.get_meta_description()

        if description == "Not Found":
            return {
                "value": description,
                "status": "Fail",
                "score": 0,
                "message": "Meta description is missing."
            }

        length = len(description)

        if 120 <= length <= 160:
            status = "Pass"
            score = 10
            message = "Meta description length is optimal."
        elif 80 <= length < 120 or 160 < length <= 180:
            status = "Warning"
            score = 7
            message = "Meta description could be improved."
        else:
            status = "Fail"
            score = 3
            message = "Meta description length is not ideal."

        return {
            "value": description,
            "length": length,
            "status": status,
            "score": score,
            "message": message,
        }

    # -------------------------------------------------
    # H1 Evaluation
    # -------------------------------------------------

    def evaluate_h1(self):
        headings = self.get_headings()

        h1 = headings["H1"]

        if len(h1) == 1:
            return {
                "count": 1,
                "status": "Pass",
                "score": 10,
                "message": "Exactly one H1 found."
            }

        if len(h1) == 0:
            return {
                "count": 0,
                "status": "Fail",
                "score": 0,
                "message": "No H1 found."
            }

        return {
            "count": len(h1),
            "status": "Warning",
            "score": 5,
            "message": "Multiple H1 tags found."
        }