import os

from services.report_generator import ReportGenerator


def export_pdf(report_data, output_dir="reports"):

    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(
        output_dir,
        "seo_audit_report.pdf"
    )

    generator = ReportGenerator(report_data)

    generator.generate_pdf(file_path)

    return file_path


def export_csv(report_data, output_dir="reports"):

    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(
        output_dir,
        "seo_audit_report.csv"
    )

    generator = ReportGenerator(report_data)

    generator.generate_csv(file_path)

    return file_path


def export_json(report_data, output_dir="reports"):

    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(
        output_dir,
        "seo_audit_report.json"
    )

    generator = ReportGenerator(report_data)

    generator.generate_json(file_path)

    return file_path