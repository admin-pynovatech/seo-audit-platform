import csv
import json

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


class ReportGenerator:

    def __init__(self, report_data: dict):

        self.report_data = report_data

    def generate_pdf(self, file_path):

        document = SimpleDocTemplate(file_path)

        styles = getSampleStyleSheet()

        elements = []

        elements.append(
            Paragraph(
                "SEO Audit Report",
                styles["Heading1"]
            )
        )

        for key, value in self.report_data.items():

            elements.append(
                Paragraph(
                    f"<b>{key}</b>: {value}",
                    styles["BodyText"]
                )
            )

        document.build(elements)

        return file_path

    def generate_csv(self, file_path):

        with open(
            file_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow(["Metric", "Value"])

            for key, value in self.report_data.items():

                writer.writerow([key, value])

        return file_path

    def generate_json(self, file_path):

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.report_data,
                file,
                indent=4
            )

        return file_path