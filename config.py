"""
Application configuration settings.

Loads environment variables from a .env file and provides
application-wide configuration constants.
"""

import os
from typing import Final

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration."""

    # ==========================================
    # Application Settings
    # ==========================================

    APP_NAME: Final[str] = os.getenv(
        "APP_NAME",
        "Website Crawler"
    )

    APP_VERSION: Final[str] = os.getenv(
        "APP_VERSION",
        "1.0.0"
    )

    DEBUG: Final[bool] = (
        os.getenv("DEBUG", "False").lower() == "true"
    )

    # ==========================================
    # HTTP Request Settings
    # ==========================================

    REQUEST_TIMEOUT: Final[int] = int(
        os.getenv("REQUEST_TIMEOUT", 10)
    )

    HEADERS: Final[dict] = {
        "User-Agent": os.getenv(
            "USER_AGENT",
            (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/138.0.0.0 Safari/537.36"
            ),
        )
    }

    # ==========================================
    # Crawler Settings
    # ==========================================

    ALLOW_REDIRECTS: Final[bool] = True

    VERIFY_SSL: Final[bool] = True

    MAX_REDIRECTS: Final[int] = 10