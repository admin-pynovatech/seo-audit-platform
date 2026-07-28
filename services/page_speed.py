import requests


class PageSpeedAnalyzer:

    BASE_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

    def __init__(self, url: str, api_key: str):

        self.url = url
        self.api_key = api_key

    def analyze(self):

        params = {
            "url": self.url,
            "key": self.api_key,
            "category": [
                "performance",
                "accessibility",
                "best-practices",
                "seo"
            ]
        }

        try:

            response = requests.get(
                self.BASE_URL,
                params=params,
                timeout=30
            )

            response.raise_for_status()

            data = response.json()

            categories = data["lighthouseResult"]["categories"]

            audits = data["lighthouseResult"]["audits"]

            return {

                "performance": int(
                    categories["performance"]["score"] * 100
                ),

                "accessibility": int(
                    categories["accessibility"]["score"] * 100
                ),

                "best_practices": int(
                    categories["best-practices"]["score"] * 100
                ),

                "seo": int(
                    categories["seo"]["score"] * 100
                ),

                "largest_contentful_paint":
                    audits["largest-contentful-paint"]["displayValue"],

                "first_contentful_paint":
                    audits["first-contentful-paint"]["displayValue"],

                "speed_index":
                    audits["speed-index"]["displayValue"],

                "total_blocking_time":
                    audits["total-blocking-time"]["displayValue"],

                "cumulative_layout_shift":
                    audits["cumulative-layout-shift"]["displayValue"]
            }

        except requests.RequestException as e:

            return {

                "error": str(e)
            }