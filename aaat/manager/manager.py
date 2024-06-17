import zipfile
import os
from aaat.manager.report_manager import ReportManager
from aaat.util.util import list_all_files_from_dir

class Manager:
    def __init__(self, output_dir, tmp_dir, report_manager, analysis_list=[]):
        self.tmp_dir = tmp_dir
        self.output_dir = output_dir
        self.report_manager = report_manager
        self.report_manager = ReportManager(output_dir)
        self.analysis_list = analysis_list
        self.unzip_specs = []
        self._find_zip_unzip_files()

    def _find_zip_unzip_files(self):
        for analysis in self.analysis_list:
            analyzers = analysis.get_analyzers()
            for analyzer in analyzers:
                related_files = analyzer.get_related_files_specs()
                main_files = analyzer.get_main_specs()
                self.unzip_specs += related_files
                self.unzip_specs += main_files

    def process(self, extraction):
        if os.path.exists(extraction):
            if os.path.isfile(extraction):
                self.process_zip(extraction)
            else:
                self.process_folder(extraction)
        else:
            print("Extraction is NONE. Nothing to process.")

    def process_zip(self, zip_file_path):
        os.makedirs(self.tmp_dir, exist_ok=True)
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            for entry in zip_ref.namelist():
                is_dir = entry.endswith('/')
                if not is_dir:
                    base_dir, file_name = os.path.split(entry)
                else:
                    base_dir = entry
                    file_name = None
                if file_name is not None:
                    for spec in self.unzip_specs:
                        if spec.matches(filename=file_name, filepath=base_dir):
                            extracted_path = zip_ref.extract(entry, self.tmp_dir)
                            print(extracted_path)
        self.process_folder(self.tmp_dir)

    def process_folder(self, folder):
        files = list_all_files_from_dir(folder)
        for file in files:
            for analysis in self.analysis_list:
                analysis.process(file)
