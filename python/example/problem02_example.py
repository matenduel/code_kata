"""
Problem02: Extract the data from MongoDB and save the data as CSV file.

Step
1. Get Credential from mariadb.ini file by using ConfigParser
    1.1 mongodb.ini located in files directory
2. Connect to MongoDB
3. Execute the query
    3.1 get revenue of each store
4. Save the return data as CSV file with column name
    4.1 save the file in "result" directory
    4.2 file name format = "%Y-%m-%d result.csv"
"""
import csv
from configparser import ConfigParser
from datetime import datetime

from pymongo import MongoClient


def main() -> None:
    # Step 1: Get Credential from mariadb.ini file by using ConfigParser
    ini_file = "files/mariadb.ini"

    config = ConfigParser()
    config.read(ini_file)

    # Step 2: Connect to MongoDB
    client = MongoClient(
        host=config["DATABASE"]["host"],
        port=int(config["DATABASE"]["port"]),
        username=config["DATABASE"]["username"],
        password=config["DATABASE"]["password"],
        readPreference="secondaryPreferred"
    )
    balis = client.balis

    # Step 3: Execute the query
    pipeline = [
        {
            "$match": {
                "order_date": {
                    "$gte": "2022-03-01 00:00:00",
                    "$lt": "2022-04-01 00:00:00"
                },
            }
        },
        {
            "$group": {
                "_id": "$shop_id",
                "revenue": {"$sum": "$sales_price"}
            }
        },
        {
            "$addFields": {
                "shop_id": "$_id"
            }
        },
        {
            "$project": {
                "_id": 0,
                "shop_id": 1,
                "revenue": 1
            }
        }
    ]
    result = balis.deliver_board.aggregate(pipeline)

    client.close()

    # Step 4: Save the return data as CSV file with column name
    file_name = f"{datetime.now().strftime('%Y-%m-%d')}-mongo-result.csv"
    fieldnames = result[0].keys()

    with open(f"result/{file_name}", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(result)


if __name__ == "__main__":
    main()



