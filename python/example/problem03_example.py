"""
Problem03: Append the data if file exists, if not create the file

Step
1. Get Credential from mariadb.ini file by using ConfigParser
    1.1 mongodb.ini located in files directory
2. Connect to MongoDB
3. Execute the query with For loop or While loop
    3.1 Get goods_no and ObjectId_list of duplicate data from terminated
    3.2 To reduce the database load, set the goods_no range
    3.3 Repeat the query to check all goods_no
    3.4 close the connection
4. Transform the data
    4.1 transform the element ObjectId_list to str
    4.2 join the list with bar("|")
5. Save the return data as CSV file with column name
    5.1 Check that file exists in "result" directory
    5.2 If not exists, create file with name format = "%Y-%m-%d result.csv"
    5.3 If exists, append the data
"""
import csv
import os
from configparser import ConfigParser
from datetime import datetime

from memory_profiler import profile
from pymongo import MongoClient


@profile
def main() -> None:
    # Step 1: Get Credential from mongodb.ini file by using ConfigParser
    ini_file = "files/mongodb.ini"

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
    hub = client.hub

    # Step 3: Execute the query
    repeat_cnt = 100
    goods_no_start = 0
    search_size = 100000

    for i in range(0, repeat_cnt):
        pipeline = [
            {
                "$match": {
                    "goods_no": {
                        "$gte": goods_no_start,
                        "$lt": goods_no_start + search_size
                    },
                }
            },
            {
                "$group": {
                    "_id": "$goods_no",
                    "cnt": {"$sum": 1},
                    "ObjectId_list": {"$push": "$_id"}
                }
            },
            {
                "$match": {
                    "cnt": {"$gt": 1}
                }
            }
        ]

        dup_list = hub.terminated.aggregate(pipeline)
        dup_list = list(dup_list)

        # Step 4: Transform the data
        for dup in dup_list:
            # change the field name in code
            dup["goods_no"] = dup.pop("_id", 0)
            # change the Type of ObjectId_list element
            dup["ObjectId_list"] = "|".join(map(str, dup["ObjectId_list"]))

        # Save when dup data exists
        if len(dup_list):
            # Step 5: Save the return data as CSV file with column name
            file_name = f"{datetime.now().strftime('%Y-%m-%d')}-mongo-result.csv"
            fieldnames = dup_list[0].keys()
            mode = "w"
            if os.path.exists(f"result/{file_name}"):
                mode = "a"

            # short version
            # mode = "w" if not os.path.exists(f"result/{file_name}") else "a"

            with open(f"result/{file_name}", mode=mode, newline="", encoding="utf-8-sig") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                # Write header if mode is "w"
                if mode == "w":
                    writer.writeheader()
                writer.writerows(dup_list)
        else:
            print(f"No dup data in range {goods_no_start} ~ {goods_no_start + search_size}")

        # Increase the goods_no_start
        goods_no_start += search_size

    client.close()


if __name__ == "__main__":
    main()
