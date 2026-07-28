"""
config.py

Centralized configuration for the SEO Audit Platform.
Loads environment variables and provides default values.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Config:
    """Application configuration."""

    # ==========================================================
    # Application
    # ==========================================================
    APP_NAME = os.getenv("APP_NAME", "SEO Audit Platform")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # ==========================================================
    # HTTP Request Settings
    # ==========================================================
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 10))

    USER_AGENT = os.getenv(
        "USER_AGENT",
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0.0.0 Safari/537.36"
        ),
    )

    HEADERS = {
        "User-Agent": USER_AGENT
    }

    # ==========================================================
    # Reports
    # ==========================================================
    PDF_REPORT_PATH = "reports/pdf"
    CSV_REPORT_PATH = "reports/csv"

    # ==========================================================
    # Streamlit
    # ==========================================================
    PAGE_TITLE = APP_NAME
    PAGE_ICON = "🔍"
    LAYOUT = "wide"

    # ==========================================================
    # SEO Score
    # ==========================================================
    MAX_SCORE = 100

    # ==========================================================
    # Supported Protocols
    # ==========================================================
    ALLOWED_SCHEMES = ("http://", "https://")