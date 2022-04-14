"""
Problem10: pandas filtering && group_by

Step
1. Get data from url
2. Delete Unnamed columns
3. Get unique value of "State", "Gender"
4. Get a sum by Gender, State.
5. Filtering with one condition
    5.1 condition => Gender = "F"
    5.2 get number of rows group by state with condition
6. Filtering with Regex
    6.1 condition => second alphabet of name is e
7. Filtering with multiple conditions
    7.1 condition => second alphabet of name is e && State = WA
"""
import pandas as pd

from memory_profiler import profile


@profile
def main() -> None:
    url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv'

    # Step 1: Get data from url

    # Step 2: Delete Unnamed columns

    # Step 3: Get unique value of "State", "Gender"

    # Step 4: Get a sum by Gender, State.

    # Step 5. Filtering with one condition

    # Step 6. Filtering with Regex

    # Step 7. Filtering with multiple conditions


if __name__ == "__main__":
    main()
