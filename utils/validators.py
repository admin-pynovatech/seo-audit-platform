from urllib.parse import urlparse


def validate_url(url: str) -> bool:
    if not url:
        return False
    try:
        result = urlparse(url)
        return all(
            [
                result.scheme in ("http", "https"),
                result.netloc,
            ]
        )
    except Exception:
        return False

    