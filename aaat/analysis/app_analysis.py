import os
from aaat.analysis.app_databases import DB_FILES_SPECS
from aaat.analysis.file_analyzers.sqlite_analyzer import DeepPackagesAnalyzer
from aaat.analysis.analysis import Analysis


class AndroidAppAnalysis(Analysis):
    def __init__(self):
        super().__init__()
        self.analyzers = []
        for key in DB_FILES_SPECS:
            file_name = DB_FILES_SPECS[key]["file_name"]
            pkg_queries = DB_FILES_SPECS[key]["pkg_queries"]
            timeline_queries = DB_FILES_SPECS[key]["timeline_queries"]
            analyzer = DeepPackagesAnalyzer(name=key, db_name=file_name, packages_queries=pkg_queries,
                                            timeline_queries=timeline_queries)
            self.analyzers.append(analyzer)

    def get_analyzers(self):
        return self.analyzers

    def process(self, file):
        directory_path, file_name = os.path.split(file)
        for analyzer in self.analyzers:
            if analyzer.can_process(filename=file_name, filepath=directory_path):
                analyzer.process(file)
