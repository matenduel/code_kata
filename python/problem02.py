"""
Problem02: Extract the data from MongoDB and save the data as CSV file.

Step
1. Get Credential from mariadb.ini file by using ConfigParser
    1.1 mongodb.ini located in files directory
2. Connect to MongoDB
3. Execute the query
    3.1 get revenue of each store
    3.2 close the connection
4. Save the return data as CSV file with column name
    4.1 save the file in "result" directory
    4.2 file name format = "%Y-%m-%d result.csv"
"""
import csv
from configparser import ConfigParser
from datetime import datetime

from memory_profiler import profile
from pymongo import MongoClient


@profile
def main() -> None:
    # Step 1: Get Credential from mariadb.ini file by using ConfigParser
    ini_file = "files/mongodb.ini"

    # Step 2: Connect to MongoDB

    # Step 3: Execute the query

    # Step 4: Save the return data as CSV file with column name


if __name__ == "__main__":
    main()
