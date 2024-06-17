from util.SQLiteDBFastLogger import SQLiteDBFastLogger

CAT_FOUND_APP_PACKAGES = "found_app_packages"
CAT_APP_TIMELINE_EVENT = "app_timeline_events"


class ReportManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ReportManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, basedir=None):
        if not hasattr(self, 'initialized'):
            self.basedir = basedir
            self.report = SQLiteDBFastLogger(basedir)
            self.report.add_logger(CAT_FOUND_APP_PACKAGES, ["pkg_name", "source_info", "analyzer"])
            self.report.add_logger(CAT_APP_TIMELINE_EVENT, ["pkg_name", "timestamp_hr", "timestamp", "event_str", "source_info", "analyzer"])
            self.initialized = True

    def log_found_app_package(self, pkg_name, source_info, analyzer):
        self.report.log_data(CAT_FOUND_APP_PACKAGES, [pkg_name, source_info, analyzer])

    def log_app_event(self, pkg_name, timestamp_hr, timestamp, event_str, source_info, analyzer):
        self.report.log_data(CAT_APP_TIMELINE_EVENT, [pkg_name, timestamp_hr, timestamp, event_str, source_info, analyzer])

    def finish_report(self):
        self.report.close()
        self.report.consolidate_database()