import time

import requests
from bs4 import BeautifulSoup

from config import Config
from utils.validators import validate_url

class WebsiteCrawler:
    def __init__(self):
        self.headers = Config.HEADERS
        self.timeout = Config.REQUEST_TIMEOUT

    def crawl(self, url: str) -> dict:
        if not validate_url(url):
            return {
                "success": False,
                "message": "Invalid URL."
            }
        try:
            start = time.perf_counter()
            response = requests.get(
                url,
                headers=self.headers,
                timeout=self.timeout,
                allow_redirects=True
            )

            end = time.perf_counter()
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
                    rel=lambda value: value and "stylesheet" in value.lower()
                )
            )

            return {
                "success": True,
                "message": "Website crawled successfully.",

                # Request Information
                "url": response.url,
                "status_code": response.status_code,
                "response_time": round(end - start, 3),
                "redirects": len(response.history),

                # Website Information
                "title": title,
                "protocol": response.url.split("://")[0].upper(),
                "content_type": response.headers.get(
                    "Content-Type",
                    "Unknown"
                ),
                "encoding": response.encoding or "Unknown",
                "server": response.headers.get(
                    "Server",
                    "Unknown"
                ),
                "content_length": response.headers.get(
                    "Content-Length",
                    f"{len(response.content)} Bytes"
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
                "message": "Request timed out."
            }

        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "message": "Unable to connect to the website."
            }

        except requests.exceptions.HTTPError as e:
            return {
                "success": False,
                "message": f"HTTP Error: {e}"
            }

        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "message": str(e)
            }

        except Exception as e:
            return {
                "success": False,
                "message": f"Unexpected Error: {e}"
            }


        