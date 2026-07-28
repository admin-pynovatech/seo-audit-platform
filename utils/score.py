"""
SEO Score Calculator
"""


class SEOScoreCalculator:

    def __init__(self, analysis: dict):

        self.analysis = analysis

    def calculate(self):

        checks = [
            self.analysis["title_analysis"],
            self.analysis["meta_analysis"],
            self.analysis["h1_analysis"],
            self.analysis["canonical_analysis"],
            self.analysis["open_graph_analysis"],
            self.analysis["language_analysis"],
            self.analysis["charset_analysis"],
        ]

        total_score = sum(item["score"] for item in checks)

        max_score = len(checks) * 10

        percentage = round((total_score / max_score) * 100)

        summary = {
            "Pass": 0,
            "Warning": 0,
            "Fail": 0
        }

        for item in checks:
            summary[item["status"]] += 1

        return {
            "seo_score": percentage,
            "total_score": total_score,
            "max_score": max_score,
            "summary": summary
        }