"""
Application Configuration

Central location for project settings.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Application configuration.
    """

    # -------------------------
    # HTTP Request Settings
    # -------------------------
    REQUEST_TIMEOUT = 10

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0.0.0 Safari/537.36"
        )
    }

    # -------------------------
    # Google PageSpeed API
    # -------------------------
    PAGE_SPEED_API_KEY = os.getenv("PAGE_SPEED_API_KEY", "")

    # -------------------------
    # Reports
    # -------------------------
    REPORTS_DIR = "reports"

    # -------------------------
    # Supported Export Formats
    # -------------------------
    EXPORT_FORMATS = [
        "PDF",
        "CSV",
        "JSON"
    ]