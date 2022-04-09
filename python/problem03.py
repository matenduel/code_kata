"""
Problem03: Append the data if file exists, if not create the file

Step
1. Get Credential from mariadb.ini file by using ConfigParser
    1.1 mongodb.ini located in files directory
2. Connect to MongoDB
3. Execute the query with For loop or While loop
    3.1 Get goods_no and ObjectId list of duplicate data from terminated
    3.2 To reduce the database load, set the goods_no range
    3.3 Repeat the query to check all goods_no
4. Save the return data as CSV file with column name
    4.1 Check that file exists in "result" directory
    4.2 If not exists, create file with name format = "%Y-%m-%d result.csv"
    4.3 If exists, append the data
"""
import csv
from configparser import ConfigParser
from datetime import datetime

from pymongo import MongoClient


def main() -> None:
    # Step 1: Get Credential from mongodb.ini file by using ConfigParser
    ini_file = "files/mongodb.ini"

    # Step 2: Connect to MongoDB

    # Step 3: Execute the query with For loop

    # Step 4: Save the return data as CSV file with column name


if __name__ == "__main__":
    main()
