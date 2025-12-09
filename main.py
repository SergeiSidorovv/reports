import tabulate

from parser_arguments import parser_arguments
from work_files import read_files
from report.work_reports import get_report

def main():
    arguments = parser_arguments()
    file_paths = arguments.files
    rows = read_files(file_paths)
    name_report = arguments.report
    report_object = get_report(name_report)
    data = report_object.generate_report(rows)

    print(tabulate.tabulate(data, headers=["Position", "Performance"]))


if __name__ == "__main__":
    main()
