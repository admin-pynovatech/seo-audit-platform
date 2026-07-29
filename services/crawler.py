"""
Website crawling service.

Handles HTTP requests, HTML parsing, and extraction
of webpage metadata and statistics.
"""

from typing import Any
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from config import Config
from utils.validators import validate_url


class WebsiteCrawler:
    """Service for crawling websites and extracting webpage information."""

    def __init__(self) -> None:
        self.headers = Config.HEADERS
        self.timeout = Config.REQUEST_TIMEOUT

    def crawl(self, url: str) -> dict[str, Any]:
        """
        Crawl a website and return webpage metadata,
        statistics, and HTTP response information.

        Args:
            url: Website URL.

        Returns:
            Dictionary containing crawl results.
        """
        if not validate_url(url):
            return {
                "success": False,
                "message": "Invalid URL.",
            }

        try:
            response = requests.get(
                url,
                headers=self.headers,
                timeout=self.timeout,
                allow_redirects=Config.ALLOW_REDIRECTS,
                verify=Config.VERIFY_SSL,
            )

            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            title = (
                soup.title.string.strip()
                if soup.title and soup.title.string
                else "No Title"
            )

            links = len(soup.find_all("a"))
            images = len(soup.find_all("img"))
            scripts = len(soup.find_all("script"))
            stylesheets = len(
                soup.find_all(
                    "link",
                    rel=lambda value: value and "stylesheet" in value.lower(),
                )
            )

            protocol = urlparse(response.url).scheme.upper()

            return {
                "success": True,
                "message": "Website crawled successfully.",
                # Request Information
                "url": response.url,
                "status_code": response.status_code,
                "response_time": round(
                    response.elapsed.total_seconds(),
                    3,
                ),
                "redirects": len(response.history),
                # Website Information
                "title": title,
                "protocol": protocol,
                "content_type": response.headers.get(
                    "Content-Type",
                    "Unknown",
                ),
                "encoding": response.encoding or "Unknown",
                "server": response.headers.get(
                    "Server",
                    "Unknown",
                ),
                "content_length": response.headers.get(
                    "Content-Length",
                    f"{len(response.content)} Bytes",
                ),
                # Page Statistics
                "links": links,
                "images": images,
                "scripts": scripts,
                "stylesheets": stylesheets,
                # HTTP Headers
                "headers": dict(response.headers),
            }

        except requests.exceptions.Timeout:
            return {
                "success": False,
                "message": "Request timed out.",
            }

        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "message": "Unable to connect to the website.",
            }

        except requests.exceptions.HTTPError as exc:
            return {
                "success": False,
                "message": f"HTTP Error: {exc}",
            }

        except requests.exceptions.RequestException as exc:
            return {
                "success": False,
                "message": str(exc),
            }

        except Exception as exc:
            return {
                "success": False,
                "message": f"Unexpected error: {exc}",
            }