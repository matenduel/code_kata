"""
Problem01: Extract the data from mariaDB and save the data as CSV file.

Step
1. Get Credential from mariadb.ini file by using ConfigParser
    1.1 mariadb.ini located in files directory
2. Connect to mariaDB
3. Execute the query
4. Save the return data as CSV file with column name with column name
    4.1 save the file in "result" directory
    4.2 file name format = "%Y-%m-%d result.csv"
"""
import csv
from configparser import ConfigParser
from datetime import datetime

import mariadb


def main() -> None:
    # Step 1: Get Credential from mariadb.ini file by using ConfigParser
    ini_file = "files/mariadb.ini"

    config = ConfigParser()
    config.read(ini_file)

    # Step 2: Connect to mariaDB
    conn = mariadb.connect(
        username=config["DATABASE"]["username"],
        password=config["DATABASE"]["password"],
        host=config["DATABASE"]["host"],
        port=config["DATABASE"]["port"],
        database=config["DATABASE"]["name"],
    )
    cur = conn.cursor()

    # Step 3: Execute the query
    query = """
        SELECT 
            goodsno,
            goodsnm
        FROM
            gd_goods
        WHERE
            goodsno <= 1000000 
    """
    cur.execute(query)
    rows = cur.fetchall()

    # connection close
    conn.close()

    # Step 4: Save the return data as CSV file with column name
    result = []
    for goodsno, goodsnm in rows:
        result.append([goodsno, goodsnm])

    file_name = f"{datetime.now().strftime('%Y-%m-%d')}-maria-result.csv"
    with open(f"result/{file_name}", 'w', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['goodsno', 'goodsnm'])
        writer.writerows(result)


if __name__ == "__main__":
    main()
