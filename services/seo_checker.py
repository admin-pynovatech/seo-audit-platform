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
        "canonical": self.get_canonical(),

        "title_analysis": self.evaluate_title(),
        "meta_analysis": self.evaluate_meta_description(),

        "h1_analysis": self.evaluate_h1(),
        "canonical_analysis": self.evaluate_canonical(),
        
        "open_graph": self.get_open_graph(),
        "open_graph_analysis": self.evaluate_open_graph(),

        "language": self.get_language(),
        "language_analysis": self.evaluate_language(),

        "charset": self.get_charset(),
        "charset_analysis": self.evaluate_charset(),

        "viewport": self.get_viewport(),
        "viewport_analysis": self.evaluate_viewport(),

        "robots": self.get_robots(),
        "robots_analysis": self.evaluate_robots(),

        
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

    # -------------------------------------------------
    # Canonical URL
    # -------------------------------------------------

    def get_canonical(self):

        canonical = self.soup.find(
            "link",
            attrs={"rel": "canonical"}
        )

        if canonical:
            return canonical.get("href", "").strip()

        return "Not Found"

    # -------------------------------------------------
    # Canonical Evaluation
    # -------------------------------------------------

    def evaluate_canonical(self):
        canonical = self.get_canonical()

        if canonical == "Not Found":
            return {
                "value": canonical,
                "status": "Fail",
                "score": 0,
                "message": "Canonical tag is missing."
            }

        if canonical.startswith("http://") or canonical.startswith("https://"):
            return {
                "value": canonical,
                "status": "Pass",
                "score": 10,
                "message": "Canonical URL is valid."
            }

        return {
            "value": canonical,
            "status": "Warning",
            "score": 5,
            "message": "Canonical URL should be absolute."
        }


    # -------------------------------------------------
    # Open Graph
    # -------------------------------------------------

    def get_open_graph(self):

        properties = [
            "og:title",
            "og:description",
            "og:image",
            "og:url",
            "og:type"
        ]

        og = {}

        for prop in properties:

            tag = self.soup.find(
                "meta",
                attrs={"property": prop}
            )

            og[prop] = tag.get("content", "").strip() if tag else "Not Found"

        return og

    # -------------------------------------------------
    # Open Graph Evaluation
    # -------------------------------------------------

    def evaluate_open_graph(self):
        og = self.get_open_graph()

        found = sum(
            value != "Not Found"
            for value in og.values()
        )

        total = len(og)

        percentage = round((found / total) * 100)

        if found == total:
            status = "Pass"
            score = 10
            message = "All Open Graph tags are present."
        elif found >= 3:
            status = "Warning"
            score = 6
            message = "Some Open Graph tags are missing."
        else:
            status = "Fail"
            score = 2
            message = "Most Open Graph tags are missing."

        return {
            "value": og,
            "found": found,
            "total": total,
            "coverage": percentage,
            "status": status,
            "score": score,
            "message": message
        }

    # -------------------------------------------------
    # HTML Language
    # -------------------------------------------------

    def get_language(self):
        html = self.soup.find("html")
        if html:
            return html.get("lang", "Not Found")

        return "Not Found"

    # -------------------------------------------------
    # HTML Language Evaluation
    # -------------------------------------------------

    def evaluate_language(self):
        language = self.get_language()
        if language == "Not Found":
            return {
                "value": language,
                "status": "Fail",
                "score": 0,
                "message": "Language attribute is missing."
            }
        return {
            "value": language,
            "status": "Pass",
            "score": 10,
            "message": "Language attribute is present."
        }

    # -------------------------------------------------
    # HTML Charset
    # -------------------------------------------------

    def get_charset(self):
        charset = self.soup.find("meta", charset=True)
        if charset:
            return charset.get("charset")
        return "Not Found"

    # -------------------------------------------------
    # HTML Charset Evaluation
    # -------------------------------------------------

    def evaluate_charset(self):
        charset = self.get_charset()
        if charset == "Not Found":
            return {
                "value": charset,
                "status": "Fail",
                "score": 0,
                "message": "Charset declaration is missing."
            }
        return {
            "value": charset,
            "status": "Pass",
            "score": 10,
            "message": "Charset is declared."
        }


    # -------------------------------------------------
    # Viewport
    # -------------------------------------------------

    def get_viewport(self):
        viewport = self.soup.find(
            "meta",
            attrs={"name": "viewport"}
        )
        if viewport:
            return viewport.get("content", "Not Found")
        return "Not Found"

    # -------------------------------------------------
    # Viewport evaluation
    # -------------------------------------------------

    def evaluate_viewport(self):
        viewport = self.get_viewport()

        if viewport == "Not Found":

            return {
                "value": viewport,
                "status": "Fail",
                "score": 0,
                "message": "Viewport meta tag is missing."
            }

        viewport_lower = viewport.lower()

        if "width=device-width" in viewport_lower:

            return {
                "value": viewport,
                "status": "Pass",
                "score": 10,
                "message": "Viewport is configured for responsive design."
            }

        return {
            "value": viewport,
            "status": "Warning",
            "score": 6,
            "message": "Viewport exists but may not be optimized for responsive design."
        }


    # -------------------------------------------------
    # Robots Meta Tag
    # -------------------------------------------------

    def get_robots(self):
        robots = self.soup.find(
            "meta",
            attrs={"name": "robots"}
        )
        if robots:
            return robots.get("content", "Not Found")
        return "Not Found"

    # -------------------------------------------------
    # Robots Meta Tag Evaluation
    # -------------------------------------------------

    def evaluate_robots(self):
        robots = self.get_robots()
        if robots == "Not Found":
            return {
                "value": robots,
                "status": "Warning",
                "score": 7,
                "message": (
                    "Robots meta tag is missing. "
                    "Most search engines default to 'index,follow', "
                    "but explicitly defining it is recommended."
                )
            }

        robots_lower = robots.lower()
        if "noindex" in robots_lower:
            return {
                "value": robots,
                "status": "Fail",
                "score": 0,
                "message": "Page is blocked from search engine indexing."
            }

        if "nofollow" in robots_lower:
            return {
                "value": robots,
                "status": "Warning",
                "score": 5,
                "message": "Links on this page are marked as 'nofollow'."
            }
        
        return {
            "value": robots,
            "status": "Pass",
            "score": 10,
            "message": "Page is configured for indexing and link following."
        }