from parser_arguments import CLI
from runner import ReportRunner

     
def main():
    cli = CLI()
    args = cli.parse()
    runner = ReportRunner(args.files, args.report)
    runner.run()


if __name__ == "__main__":
    main()
