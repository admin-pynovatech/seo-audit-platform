"""
Website Crawler

Responsible for downloading webpages and returning
structured information for SEO analysis.
"""

import time

import requests
from bs4 import BeautifulSoup

from config import Config
from utils.validators import validate_url


class WebsiteCrawler:
    """Website crawler."""

    def __init__(self):
        self.headers = Config.HEADERS
        self.timeout = Config.REQUEST_TIMEOUT

    def crawl(self, url: str) -> dict:
        """
        Crawl a website and return structured data.
        """

        if not validate_url(url):
            return {
                "success": False,
                "message": "Invalid URL"
            }

        try:

            start_time = time.perf_counter()

            response = requests.get(
                url,
                headers=self.headers,
                timeout=self.timeout
            )

            end_time = time.perf_counter()

            soup = BeautifulSoup(
                response.text,
                "lxml"
            )

            return {
                "success": True,
                "url": response.url,
                "status_code": response.status_code,
                "response_time": round(end_time - start_time, 3),
                "html": response.text,
                "soup": soup,
                "message": "Website crawled successfully."
            }

        except requests.exceptions.Timeout:

            return {
                "success": False,
                "message": "Request timeout."
            }

        except requests.exceptions.ConnectionError:

            return {
                "success": False,
                "message": "Connection error."
            }

        except requests.exceptions.RequestException as e:

            return {
                "success": False,
                "message": str(e)
            }