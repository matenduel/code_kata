"""
Problem06: Save the daily order data in the directory(format: yyyy/mm/dd)

Step
1. Get goods_list and order_list from csv file
    1.1 Use pandas
    1.2 Both files are CSV file
2. Transform the data type of order_date to Datetime
    2.1 Consider an order_date as a UTC date
3. Join the goods data and order data
4. Find un-duplicated column name
5. Save the daily order data in directory(order/yyyy/mm/dd)
    5.1 Create the directory if not exist
    5.2 Do not create the directory if there is no order on that day
    5.3 Do not save the duplicated colum
"""
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path


def main() -> None:
    # file_path
    goods_list_file = "./files/goods_list.csv"
    order_list_file = "./files/order_list.csv"

    # Step 1: Get goods_list and order_list from csv file by using pandas

    # Step 2: Transform the data type of order_date to Datetime

    # Step 3: Join the goods data and order data

    # Step 4: Find un-duplicated column name

    # Step 5: Save the daily order data in directory(yyyy/mm/dd)


if __name__ == "__main__":
    main()
