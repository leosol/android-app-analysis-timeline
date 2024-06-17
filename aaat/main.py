import argparse
import logging
import os.path
import signal
import sys
from aaat.manager.manager import Manager
from aaat.manager.report_manager import ReportManager
from aaat.analysis.app_analysis import AndroidAppAnalysis
from util.util import destroy_dir_files


def signal_handler(signal, frame):
    print('You pressed Ctrl+C! Exiting gracefully.')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def parse_args():
    parser = argparse.ArgumentParser(description="Start Android App Analysis",
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("--debug", action="store_true", dest="debug_mode",
                        help="Run in debug mode (dump debug messages).")
    parser.add_argument("-extraction", action="store", dest="extraction", required=False,
                        help="The extraction. A zip file or a folder that contains the extracted android files")
    parser.add_argument("-temp", action="store", dest="temp_dir", required=False,
                        default="./temp/",
                        help="The temp dir to use for temporary files")
    parser.add_argument("-out", action="store", dest="out_dir", required=False,
                        default='./output',
                        help="The output dir to use for the database report")
    parser.add_argument("--force", action="store_true", dest="force", required=False,
                        default=False,
                        help="Overwrite output dir. All existing files will be destroyed.")
    options = parser.parse_args()
    return options


def main():
    opts = parse_args()
    extraction = opts.extraction
    temp = opts.temp_dir
    output = opts.out_dir
    logging.basicConfig(level=logging.DEBUG if opts.debug_mode else logging.INFO)
    if os.path.exists(temp):
        destroy_dir_files(temp)
        os.makedirs(temp)
    else:
        os.makedirs(temp)
    if os.path.exists(output):
        if opts.force:
            destroy_dir_files(output)
            os.makedirs(output)
        else:
            print(f"Output file exists. Overwrite? use --force to overwrite.")
            sys.exit(0)
    else:
        os.makedirs(output)
    report_manager = ReportManager(basedir=output)
    manager = Manager(output_dir=output, tmp_dir=temp, report_manager=report_manager,
                      analysis_list=[AndroidAppAnalysis()])
    manager.process(extraction)
    report_manager.finish_report()



if __name__ == "__main__":
    main()
