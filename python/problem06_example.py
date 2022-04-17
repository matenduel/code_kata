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
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
from memory_profiler import profile


@profile
def main() -> None:
    # file_path
    goods_list_file = "./files/goods_list.csv"
    order_list_file = "./files/order_list.csv"

    # Step 1: Get goods_list and order_list from csv file by using pandas
    goods_list = pd.read_csv(goods_list_file)
    order_list = pd.read_csv(order_list_file)

    # Step 2: Transform the data type of order_date to Datetime
    order_list["order_date"] = order_list["order_date"].map(lambda x: datetime.strptime(x, "%Y-%m-%d"))

    # Step 3: Join the goods data and order data
    merged_data = pd.merge(
        order_list, goods_list, left_on="goods_no", right_on="goods_no", how="left", suffixes=('', '_drop')
    )
    sorted_data = merged_data.sort_values(by="order_date", ascending=True)

    # Step 4: Find un-duplicated column name
    columns = [column for column in sorted_data.columns if not column.endswith("_drop")]

    # Step 5: Save the daily order data in directory(yyyy/mm/dd)
    min_date = sorted_data["order_date"].iloc[0]
    max_date = sorted_data["order_date"].iloc[-1]
    period = (max_date - min_date).days

    for day in range(period + 1):
        select_datetime = min_date + timedelta(days=day)
        conditions = (
            (sorted_data['order_date'] >= select_datetime) &
            (sorted_data['order_date'] < select_datetime + timedelta(days=1))
        )
        # Get daily order data
        daily_order_data = sorted_data.loc[conditions]

        if len(daily_order_data) > 0:
            directory_path = f"order_data/{select_datetime.year}/{select_datetime.month}/{select_datetime.day}"
            # Create directory
            Path(directory_path).mkdir(parents=True, exist_ok=True)
            # Save the data without duplicated column
            daily_order_data.to_csv(f'{directory_path}/order.csv', header=True, index=False, columns=columns)


if __name__ == "__main__":
    main()
