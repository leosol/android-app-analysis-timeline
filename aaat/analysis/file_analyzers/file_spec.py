import re

MATCH_MODE_FILENAME = 0
MATCH_MODE_PATH = 1
MATCH_MODE_BOTH = 2
MATCH_MODE_FILENAME_PATTERN = 3
MATCH_MODE_PATH_PATTERN = 4
MATCH_MODE_BOTH_PATTERNS = 5


class FileSpec:
    def __init__(self, filename, path, match_mode=MATCH_MODE_FILENAME, ignore_case=True):
        self.filename = filename
        self.path = path
        self.match_mode = match_mode
        self.ignore_case = ignore_case

    def matches(self, filename, filepath):
        if self.match_mode == MATCH_MODE_FILENAME and (
                self.filename == filename or (self.ignore_case and self.filename.lower() == filename.lower())):
            return True
        if self.match_mode == MATCH_MODE_PATH and (
                self.path == filepath or (self.ignore_case and self.path.lower() == filepath.lower())):
            return True
        if self.match_mode == MATCH_MODE_BOTH and (
                (self.filename == filename or (self.ignore_case and self.filename.lower() == filename.lower())) and (
                self.path == filepath or (self.ignore_case and self.path.lower() == filepath.lower()))):
            return True
        if self.match_mode == MATCH_MODE_FILENAME_PATTERN:
            raise NotImplementedError()
        if self.match_mode == MATCH_MODE_PATH_PATTERN:
            raise NotImplementedError()
        if self.match_mode == MATCH_MODE_BOTH_PATTERNS:
            raise NotImplementedError()
        return False



