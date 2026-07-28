"""
Website Crawler

Responsible for downloading webpages and extracting
basic website information.

This module DOES NOT calculate SEO scores.
"""

import time

import requests

from config import Config
from utils.validators import validate_url
from services.seo_checker import SEOAnalyzer


class WebsiteCrawler:

    def __init__(self):
        self.headers = Config.HEADERS
        self.timeout = Config.REQUEST_TIMEOUT

    def crawl(self, url: str) -> dict:

        if not validate_url(url):
            return {
                "success": False,
                "message": "Invalid URL"
            }

        try:
            start = time.perf_counter()

            response = requests.get(
                url,
                headers=self.headers,
                timeout=self.timeout,
                allow_redirects=True
            )

            response.raise_for_status()

            end = time.perf_counter()

            seo = SEOAnalyzer(response.text)
            seo_data = seo.analyze()

            return {
                "success": True,
                "url": response.url,
                "status_code": response.status_code,
                "response_time": round(end - start, 3),
                **seo_data,
                "message": "Website crawled successfully."
            }

        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "message": str(e)
            }