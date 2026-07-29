"""
Validation utilities for the Website Crawler.
"""

from urllib.parse import urlparse


def validate_url(url: str) -> bool:
    """
    Validate whether a URL is a valid HTTP or HTTPS address.

    Args:
        url: URL to validate.

    Returns:
        True if the URL is valid, otherwise False.
    """
    if not url:
        return False

    try:
        parsed_url = urlparse(url)

        return (
            parsed_url.scheme in {"http", "https"}
            and bool(parsed_url.netloc)
        )

    except Exception:
        return False