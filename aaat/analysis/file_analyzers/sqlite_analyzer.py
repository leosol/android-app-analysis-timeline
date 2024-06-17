import sqlite3
import traceback
from abc import abstractmethod
from aaat.analysis.file_analyzers.file_analyzer import FileAnalyzer, SPECS_MATCH_ALL
from aaat.analysis.file_analyzers.file_spec import FileSpec, MATCH_MODE_FILENAME


def _create_sqlite_db_specs(database_name):
    specs = []
    specs.append(FileSpec(filename=database_name, path=None, match_mode=MATCH_MODE_FILENAME))
    specs.append(FileSpec(filename=f"{database_name}-journal", path=None, match_mode=MATCH_MODE_FILENAME))
    specs.append(FileSpec(filename=f"{database_name}-shm", path=None, match_mode=MATCH_MODE_FILENAME))
    specs.append(FileSpec(filename=f"{database_name}-wal", path=None, match_mode=MATCH_MODE_FILENAME))
    related_files_specs = specs
    main_spec = specs[0]
    return [main_spec], related_files_specs


class GenericSQLITEAnalyzer(FileAnalyzer):
    def __init__(self, database_name):
        self.database_name = database_name
        main_specs, related_specs = _create_sqlite_db_specs(database_name)
        super().__init__(main_specs=main_specs, related_files_specs=related_specs)

    def process(self, filepath):
        try:
            conn = sqlite3.connect(filepath)
            self.process_sqlite_file(conn)
            conn.close()
        except Exception:
            traceback.print_exc()


    @abstractmethod
    def process_sqlite_file(self, connection):
        raise NotImplementedError


class DeepPackagesAnalyzer(GenericSQLITEAnalyzer):

    def __init__(self, name, db_name, packages_queries=[], timeline_queries=[]):
        super().__init__(db_name)
        self.name = name
        self.packages_queries = packages_queries
        self.timeline_queries = timeline_queries
        self.current_file = None

    def process(self, filepath):
        self.current_file = filepath
        super().process(filepath=filepath)

    def process_sqlite_file(self, connection):
        pakages = set()
        timeline = []
        for pkg_query in self.packages_queries:
            cursor = connection.cursor()
            try:
                cursor.execute(pkg_query)
                rows = cursor.fetchall()
                for row in rows:
                    pakages.add(row[0])
            except Exception:
                traceback.print_exc()
                print(f"Wrong query for: {self.current_file}")
                print(f"Query: {pkg_query}")

        for timeline_query in self.timeline_queries:
            cursor = connection.cursor()
            try:
                cursor.execute(timeline_query)
                rows = cursor.fetchall()
                for row in rows:
                    timeline.append(row)
            except Exception:
                traceback.print_exc()
                print(f"Wrong query for: {self.current_file}")
                print(f"Query: {timeline_query}")

        for pkg in pakages:
            self.report_manager.log_found_app_package(pkg_name=pkg, source_info=self.database_name, analyzer=self.name)
        for timeline_event in timeline:
            pkg = timeline_event[0]
            timestamp_hr = timeline_event[1]
            timestamp = timeline_event[2]
            event_str = timeline_event[3]
            self.report_manager.log_app_event(pkg_name=pkg, timestamp_hr=timestamp_hr, timestamp=timestamp,
                                              event_str=event_str, source_info=self.database_name, analyzer=self.name)
