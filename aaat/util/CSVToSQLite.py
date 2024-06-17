from pathlib import Path
import subprocess
import os
import sqlite3
import re


def abbreviate_string(input_string):
    words = input_string.split('_')
    abbreviation = ''.join(word[0] for word in words)
    return abbreviation


class CSVToSQLite:
    def __init__(self, dest_dir, db_file_name="main.db"):
        self.dest_dir = dest_dir
        self.db_file_name = db_file_name
        self.db_file_path = os.path.join(self.dest_dir, self.db_file_name)
        print(f"Database file {self.db_file_path}")

    def create_table(self, csv_file, table_name):
        first_line = ""
        with open(csv_file) as f:
            first_line = f.readline()

        tokens = re.split('[,;]', first_line)
        tokens = [re.sub(r'[ #/()-]', '_', token) for token in tokens]
        column_names = []
        empty_column_count = 1
        for item in tokens:
            if len(item) == 0:
                column_names.append(f"unknown_{empty_column_count}")
                empty_column_count += 1
            else:
                column_names.append(item)

        output_string = ','.join(column_names)
        sql = "CREATE TABLE IF NOT EXISTS "+table_name+" ("+output_string+")"
        #print(sql)
        con = sqlite3.connect(self.db_file_path)
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        con.close()
        return column_names

    def create_indexes(self, column_names, table_name):
        con = sqlite3.connect(self.db_file_path)
        cur = con.cursor()
        for column_name in column_names:
            abbreviation = abbreviate_string(table_name)
            str_idx_creation = f"create index if not exists idx_{abbreviation}_{column_name} on {table_name}({column_name})"
            con.execute(str_idx_creation)
        con.commit()
        con.close()

    def import_csv_to_sqlite(self, csv_file, table_name, separator=',', skip_first_line=True):
        csv_file_path = str(csv_file).replace('\\', '\\\\')
        result = subprocess.run([
            "sqlite3",
            "-separator",
            f"'{separator}'",
            f"{self.db_file_path}",
            "-cmd",
            ".mode csv",
            f".import --skip 1 {csv_file_path} {table_name}",
            ], capture_output=False)
        if result.returncode == 0:
            print(f"{csv_file} Imported into database {self.db_file_path}")
        else:
            print(f"Failed to import {csv_file}")

    def import_csv_dir_into_database(self, csv_dir):
        csv_files = {}
        stack = [csv_dir]
        while stack:
            current_directory = stack.pop()
            for filename in os.listdir(current_directory):
                file_path = os.path.join(current_directory, filename)
                if os.path.isdir(file_path):
                    stack.append(file_path)
                else:
                    if filename.endswith(".csv"):
                        csv_files[file_path] = file_size = os.path.getsize(file_path)
                        
        sorted_csv_files = {k: v for k, v in sorted(csv_files.items(), key=lambda item: item[1], reverse=True)}
        for csv_file_path, csv_file_size in sorted_csv_files.items():
            print(f"Importing {csv_file_path} into database {self.db_file_name}")
            file_name = os.path.basename(csv_file_path)
            basename = os.path.splitext(file_name)[0]
            table_name = basename.replace(' ', '_').replace('.', '_')
            column_names = self.create_table(csv_file_path, table_name)
            self.import_csv_to_sqlite(csv_file_path, table_name, ",", True)
            self.create_indexes(column_names, table_name)


