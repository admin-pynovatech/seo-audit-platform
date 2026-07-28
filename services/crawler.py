"""
Website Crawler

Responsible for downloading a webpage
and returning structured information.

This module DOES NOT perform SEO analysis.
"""

import requests

from bs4 import BeautifulSoup

from config import Config
from utils.validators import validate_url


class WebsiteCrawler:
    """Website crawler."""

    def __init__(self):
        self.headers = Config.HEADERS
        self.timeout = Config.REQUEST_TIMEOUT

    def crawl(self, url: str):
        """
        Crawl a website.

        Parameters
        ----------
        url : str

        Returns
        -------
        dict
        """

        if not validate_url(url):
            return {
                "success": False,
                "message": "Invalid URL",
            }

        # HTTP request will be implemented next
        return {
            "success": True,
            "message": "Crawler initialized successfully.",
        }