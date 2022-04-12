"""
Problem01: Extract the data from mariaDB and save the data as CSV file.

Step
1. Get Credential from mariadb.ini file by using ConfigParser
    1.1 mariadb.ini located in files directory
2. Connect to mariaDB
3. Execute the query
    3.1 close the connection
4. Save the return data as CSV file with column name
    4.1 save the file in "result" directory
    4.2 file name format = "%Y-%m-%d result.csv"
"""
import csv
from configparser import ConfigParser
from datetime import datetime

import mariadb
from memory_profiler import profile


@profile
def main() -> None:
    # Step 1: Get Credential from mariadb.ini file by using ConfigParser
    ini_file = "files/mariadb.ini"

    # Step 2: Connect to mariaDB

    # Step 3: Execute the query

    # Step 4: Save the return data as CSV file with column name


if __name__ == "__main__":
    main()
