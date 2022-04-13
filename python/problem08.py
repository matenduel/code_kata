"""
Problem08: Convert Naive Datetime to Aware Datetime

Step
1. Print the date(format: %Y-%m-%d) of datetime
    1.1 utc_datetime and kst_datetime
    1.2 datetime_without_tz
2. Calculate the time difference between utc_datetime and kst_datetime
    2.1
3. Compare the utc_datetime and kst_datetime
    3.1 Use >, ==, <
4. Compare the utc_datetime and datetime_without_tz
    3.1 Use >, ==, <
5. Convert Naive_datetime(datetime_without_tz) to Aware_datetime
    5.1 use KST timezone && replace function
6. Get KST Date from utc_datetime
"""
from datetime import datetime, timezone, timedelta

from memory_profiler import profile

KST = timezone(timedelta(hours=9))


@profile
def main() -> None:
    # Aware datetime = contain timezone info
    utc_datetime = datetime(year=2022, month=4, day=10, hour=19, tzinfo=timezone.utc)
    kst_datetime = datetime(year=2022, month=4, day=11, hour=4, tzinfo=KST)

    # Naive datetime = No timezone info
    datetime_without_tz = datetime.now()

    # Step 1: Print the date(format: %Y-%m-%d) of utc_datetime and kst_datetime
    # Aware
    print("utc_datetime: ", )
    print("kst_datetime: ", )
    # Naive
    print("datetime_without_tz: ", )

    # Step 2: Calculate the time difference between utc_datetime and kst_datetime
    print("time difference: ", )

    # Step 3: Compare the utc_datetime and kst_datetime.
    # Use >, ==, <

    # Step 4: Compare the utc_datetime and kst_datetime.
    # Error occur!!!
    try:
        print(utc_datetime == datetime_without_tz)
    except TypeError as e:
        print("Error Occur!!!!")
        print("Can't compare the aware and naive")
        print(e)

    # Step 5: Convert Naive_datetime(datetime_without_tz) to Aware_datetime
    print("before: ", )
    print("after: ", )

    # Step 6: Get KST Date from utc_datetime


if __name__ == "__main__":
    main()

