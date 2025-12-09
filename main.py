from parser_arguments import parser_arguments
from work_files import read_files


def main():
    arguments = parser_arguments()
    file_paths = arguments.files
    rows = read_files(file_paths)
    return


if __name__ == "__main__":
    main()
