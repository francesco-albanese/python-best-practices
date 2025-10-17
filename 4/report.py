from abc import ABC, abstractmethod
from typing import List, Dict
import json

class ReportFormatter(ABC):
    @abstractmethod
    def format(self, data: List[Dict]) -> str:
        pass

class TextFormatter(ReportFormatter):
    def format(self, data: List[Dict]) -> str:
        report = ""
        for item in data:
            report += f"Name: {item.get('name', 'N/A')}, Value: {item.get('value', 'N/A')}\n"
        return report

class CSVFormatter(ReportFormatter):
    def format(self, data: List[Dict]) -> str:
        if not data:
            return ""
        headers = data[0].keys()
        report = ",".join(headers) + "\n"
        for item in data:
            values = [str(item.get(h, "")) for h in headers]
            report += ",".join(values) + "\n"
        return report

class HTMLFormatter(ReportFormatter):
    def format(self, data: List[Dict]) -> str:
        if not data:
            return "<table></table>"
            
        headers = "".join([f"<th>{key}</th>" for key in data[0].keys()])
        
        rows = ""
        for row_data in data:
            cells = "".join([f"<td>{row_data.get(key, '')}</td>" for key in data[0].keys()])
            rows += f"<tr>{cells}</tr>"
            
        return f"<table><thead><tr>{headers}</tr></thead><tbody>{rows}</tbody></table>"

class JSONFormatter(ReportFormatter):
    def format(self, data: List[Dict]) -> str:
        return json.dumps(data, indent=2)

class ReportGenerator:
    def __init__(self, formatter: ReportFormatter):
        self.formatter = formatter

    def generate(self, data: List[Dict]) -> str:
        return self.formatter.format(data)

    def set_formatter(self, formatter: ReportFormatter):
        self.formatter = formatter

if __name__ == '__main__':
    sample_data = [
        {'name': 'Metric 1', 'value': 100},
        {'name': 'Metric 2', 'value': 200},
        {'name': 'Metric 3', 'value': 150}
    ]

    # Initialize with TextFormatter
    report_generator = ReportGenerator(TextFormatter())
    print("--- Text Report ---")
    print(report_generator.generate(sample_data))

    # Change to CSVFormatter
    report_generator.set_formatter(CSVFormatter())
    print("--- CSV Report ---")
    print(report_generator.generate(sample_data))

    # Change to HTMLFormatter
    report_generator.set_formatter(HTMLFormatter())
    print("--- HTML Report ---")
    print(report_generator.generate(sample_data))

    # Change to JSONFormatter
    report_generator.set_formatter(JSONFormatter())
    print("--- JSON Report ---")
    print(report_generator.generate(sample_data))