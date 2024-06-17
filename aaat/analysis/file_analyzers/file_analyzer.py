from abc import abstractmethod
from aaat.manager.report_manager import ReportManager

SPECS_MATCH_ALL = 0
SPECS_MATCH_ANY = 1


class FileAnalyzer:
    def __init__(self, main_specs, related_files_specs=[], match_mode=SPECS_MATCH_ANY):
        self.related_files_specs = related_files_specs
        self.main_specs = main_specs
        self.match_mode = match_mode
        self.report_manager = ReportManager()

    def can_process(self, filename, filepath):
        qtd_matches = 0
        for item in self.main_specs:
            if item.matches(filename, filepath):
                qtd_matches = qtd_matches + 1
        if self.match_mode == SPECS_MATCH_ANY:
            return qtd_matches > 0
        if self.match_mode == SPECS_MATCH_ALL:
            return qtd_matches == len(self.main_specs)
        return False

    def get_related_files_specs(self):
        return self.related_files_specs

    def get_main_specs(self):
        return self.main_specs

    @abstractmethod
    def process(self, filepath):
        raise NotImplementedError
