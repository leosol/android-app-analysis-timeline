
_FI_KEY = "file_name"
_PK_KEY = "pkg_queries"
_TL_KEY = "timeline_queries"

DB_FILES_SPECS = {
        #'com.android.vending.1': {
        #        _FI_KEY: 'streamdatastore.db',
        #        _PK_KEY: ["select distinct(id) from streamdata WHERE id glob '[A-Za-z]*' and id like '%.%' "
        #                  "and id not like '%/%' and id not like '%?%'"],
        #        _TL_KEY: []
        #},
        "com.android.vending.2": {
                _FI_KEY: 'auto_update.db',
                _PK_KEY: ["select distinct(pk) from auto_update WHERE pk glob '[A-Za-z]*' and pk like '%.%' "
                          "and pk not like '%/%' and pk not like '%?%'"],
                _TL_KEY: []
        },
        "com.android.vending.3": {
                _FI_KEY: 'client_reviews_cache.db',
                _PK_KEY: ["select distinct(doc_id) from client_reviews_cache_store WHERE doc_id glob '[A-Za-z]*' "
                          "and doc_id like '%.%' and doc_id not like '%/%' and doc_id not like '%?%'"],
                _TL_KEY: ["select doc_id, strftime('%Y/%m/%d  %H:%M', datetime(timestamp/1000, 'unixepoch')) as timestamp, "
                          "timestamp, 'client review' as event_str "
                          "from client_reviews_cache_store "
                          "WHERE doc_id glob '[A-Za-z]*' and doc_id like '%.%' and doc_id not like '%/%' and doc_id not like '%?%'"]
        },
        "com.android.vending.4": {
                _FI_KEY: 'install_queue.db',
                _PK_KEY: ["select distinct(pk) from install_requests WHERE pk glob '[A-Za-z]*' "
                          "and pk like '%.%' and pk not like '%/%' and pk not like '%?%'"],
                _TL_KEY: []
        },
        "com.android.vending.5": {
                _FI_KEY: 'install_source.db',
                _PK_KEY: ["select distinct(pk) from install_source WHERE pk glob '[A-Za-z]*' "
                          "and pk like '%.%' and pk not like '%/%' and pk not like '%?%'"],
                _TL_KEY: []
        },
        "com.android.vending.6": {
                _FI_KEY: 'library.db',
                _PK_KEY: ["select distinct(doc_id) from ownership WHERE doc_id glob '[A-Za-z]*' "
                          "and doc_id like '%.%' and doc_id not like '%/%' and doc_id not like '%?%'"],
                _TL_KEY: ["select doc_id, strftime('%Y/%m/%d  %H:%M', datetime(purchase_time/1000, 'unixepoch')) as timestamp, purchase_time, "
                          "'purchase_time' as event from ownership WHERE doc_id glob '[A-Za-z]*' "
                          "and doc_id like '%.%' and doc_id not like '%/%' and doc_id not like '%?%'"]
        },
        "com.android.vending.7": {
                _FI_KEY: 'localappstate.db',
                _PK_KEY: ["select distinct(package_name) from appstate WHERE package_name glob '[A-Za-z]*' "
                          "and package_name like '%.%' and package_name not like '%/%' and package_name not like '%?%'"],
                _TL_KEY: ["""select package_name,
                        	    strftime('%Y/%m/%d  %H:%M', datetime(first_download_ms/1000, 'unixepoch')) as timestamp, first_download_ms, 
	                            'first_download_ms' as event
                                from appstate WHERE package_name glob '[A-Za-z]*' and package_name like '%.%' 
                                and package_name not like '%/%' and package_name not like '%?%'""",
                          """ select package_name,
                                    strftime('%Y/%m/%d  %H:%M', datetime(last_update_timestamp_ms/1000, 'unixepoch')) as timestamp, last_update_timestamp_ms, 
                                    'last_update_timestamp_ms' as event
                                 from appstate WHERE package_name glob '[A-Za-z]*' and package_name like '%.%' 
                                 and package_name not like '%/%' and package_name not like '%?%'"""]
        },
        "com.android.vending.8": {
                _FI_KEY: 'session_constraints.db',
                _PK_KEY: ["select distinct(pk) from app_data WHERE pk glob '[A-Za-z]*' "
                          "and pk like '%.%' and pk not like '%/%' and pk not like '%?%'"],
                _TL_KEY: []
        },
        "com.android.vending.9": {
                _FI_KEY: 'xternal_referrer_status.db',
                _PK_KEY: ["select distinct(pk) from external_referrer_status_store WHERE pk glob '[A-Za-z]*' "
                          "and pk like '%.%' and pk not like '%/%' and pk not like '%?%'"],
                _TL_KEY: []
        },
        "com.google.android.gms.1":{
                _FI_KEY: 'gass.db',
                _PK_KEY: ["select distinct(package_name) from app_info WHERE package_name glob '[A-Za-z]*' "
                          "and package_name like '%.%' and package_name not like '%/%' and package_name not like '%?%'"],
                _TL_KEY: []
        },
        "com.google.android.gms.2":{
                _FI_KEY: 'google_app_measurement.db',
                _PK_KEY: ["select distinct(app_id) from apps WHERE app_id glob '[A-Za-z]*' "
                          "and app_id like '%.%' and app_id not like '%/%' and app_id not like '%?%'",
                          "select distinct(app_id) from app2 WHERE app_id glob '[A-Za-z]*' "
                          "and app_id like '%.%' and app_id not like '%/%' and app_id not like '%?%'"],
                _TL_KEY: ["""select app_id, 
                    strftime('%Y/%m/%d  %H:%M', datetime(last_fire_timestamp/1000, 'unixepoch')) as timestamp, last_fire_timestamp, 
                    'last_fire_timestamp' as event
                from events WHERE app_id glob '[A-Za-z]*' and app_id like '%.%' and app_id not like '%/%' and app_id not like '%?%'"""]
        },
        "com.samsung.android.app.galaxyfinder.1":{
                _FI_KEY: 'Application.db',
                _PK_KEY: ["select DISTINCT(package) from launch_app_info",
                          "select DISTINCT(package) from alias_info",
                          "select DISTINCT(package) from package_list"],
                _TL_KEY: ["""select package, 
                            strftime('%Y/%m/%d  %H:%M', datetime(launch_time/1000, 'unixepoch')) as timestamp, launch_time, 
                            'launch_time' as event
                        from launch_app_info"""]
        },
        "com.samsung.android.bixby.agent.1":{
                _FI_KEY: 'pdsSync.db',
                _PK_KEY: ["select DISTINCT(package) from application"],
                _TL_KEY: []
        },
        "com.samsung.android.fast.1":{
                _FI_KEY: 'secure_wifi.db',
                _PK_KEY: ["SELECT DISTINCT(package) from apps"],
                _TL_KEY: [""""""]
        },
        "com.samsung.android.forest.1": {
                _FI_KEY: 'dwbCommon.db',
                _PK_KEY: ["SELECT DISTINCT(name) from foundPackages"],
                _TL_KEY: ["""SELECT a.name, strftime('%Y/%m/%d  %H:%M', datetime(b.timeStamp/1000, 'unixepoch')) as timestamp, b.timeStamp, 
                'usageEvents' as event from foundPackages a inner join usageEvents b on a.pkgId=b.pkgId"""]
        },
        "com.samsung.android.game.gos.1": {
                _FI_KEY: 'categoryInfo.db',
                _PK_KEY: ["select DISTINCT(pkgName) from CategoryInfo"],
                _TL_KEY: []
        },
        "com.samsung.android.sm.policy.1":{
                _FI_KEY: 'scpm.db',
                _PK_KEY: ["select DISTINCT(category) from FoldablePackagePolicy",
                          "select DISTINCT(category) from FoldablePackagePolicy_B2"],
                _TL_KEY: [""""""]
        },
        "com.samsung.android.smartsuggestions":{
                _FI_KEY: 'DataObserver.db',
                _PK_KEY: ["SELECT DISTINCT(package) from AppItem"],
                _TL_KEY: ["""SELECT package, 
                            strftime('%Y/%m/%d  %H:%M', datetime(created_ts/1000, 'unixepoch')) as timestamp, created_ts, 
                            'Samsung SmartSuggestions created' as Event
                        from AppItem""",
                        """SELECT package, 
                            strftime('%Y/%m/%d  %H:%M', datetime(updated_ts/1000, 'unixepoch')) as timestamp, updated_ts,
                            'Samsung SmartSuggestions updated' as Event
                        from AppItem"""]
        },
        "com.sec.android.app.shealth":{
                _FI_KEY: 'HealthPlain.db',
                _PK_KEY: ["select distinct(name) from installed_packages"],
                _TL_KEY: ["""select name,
                                    strftime('%Y/%m/%d  %H:%M', datetime(last_update_time/1000, 'unixepoch')) as last_update_time, last_update_time, 
                                    ('Health Plain - app version: '|| version) as event
                                from installed_packages"""]
        },
        "com.sec.android.provider.badge":{
                _FI_KEY: 'badge.db',
                _PK_KEY: ["SELECT DISTINCT(package) from apps"],
                _TL_KEY: [""""""]
        },
        "com.sec.android.sdhms":{
                _FI_KEY: 'thermal_log',
                _PK_KEY: ["select DISTINCT(package_name) from NETSTAT"],
                _TL_KEY: ["""select package_name,
                                strftime('%Y/%m/%d  %H:%M', datetime(start_time/1000, 'unixepoch')) as timestamp, start_time, 
                                'Network Usage: '||+net_usage as event
                                from NETSTAT"""]
        },
        "System.1":{
                _FI_KEY: 'PkgPredictions.db',
                _PK_KEY: ["select DISTINCT REPLACE(user_pkg, '_&_0', '') as id from tbl_PkgSummary",
                          "select DISTINCT previous_one from tbl_Sample",
                          "select DISTINCT previous_two from tbl_Sample",
                          "select DISTINCT previous_three from tbl_Sample",
                          "select DISTINCT running_pkg from tbl_Sample"],
                _TL_KEY: ["""select REPLACE(user_pkg, '_&_0', '') as id,
                                    strftime('%Y/%m/%d  %H:%M', datetime(time_add/1000, 'unixepoch')) as timestamp, time_add,
                                    'dex_compiled' as event
                                from tbl_PkgSummary""",
                          """select 
                                    running_pkg,
                                    strftime('%Y/%m/%d  %H:%M', datetime(launch_time/1000, 'unixepoch')) as timestamp, launch_time, 
                                    'launch_time' as event
                                from tbl_Sample"""]
        }

}





