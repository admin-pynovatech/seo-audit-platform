import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_NAME = os.getenv(
        "APP_NAME",
        "Website Crawler"
    )

    APP_VERSION = os.getenv(
        "APP_VERSION",
        "1.0.0"
    )

    DEBUG = os.getenv(
        "DEBUG",
        "False"
    ).lower() == "true"

    # -------------------------
    # HTTP Request Settings
    # -------------------------
    REQUEST_TIMEOUT = int(
        os.getenv("REQUEST_TIMEOUT", 10)
    )

    HEADERS = {
        "User-Agent": os.getenv(
            "USER_AGENT",
            (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/138.0.0.0 Safari/537.36"
            ),
        )
    }

    # -------------------------
    # Crawler Settings
    # -------------------------
    ALLOW_REDIRECTS = True

    VERIFY_SSL = True

    MAX_REDIRECTS = 10