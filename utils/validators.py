from urllib.parse import urlparse


def validate_url(url: str) -> bool:
    """
    Validate whether a URL is correctly formatted.

    Parameters
    ----------
    url : str
        Website URL provided by the user.

    Returns
    -------
    bool
        True if valid, otherwise False.
    """

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