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
    baby_names = pd.read_csv(url)
    print(baby_names.info())

    # Step 2: Delete Unnamed columns
    column_names = baby_names.columns
    for col_name in column_names:
        if "Unnamed" in col_name:
            del baby_names[col_name]

    # Step 3: Get unique value of "State", "Gender"
    print(baby_names["Gender"].unique())
    print(baby_names["State"].unique())

    # Step 4: Get a sum by Gender, State.
    sub = baby_names.loc[:, ["State", "Gender", "Count"]]
    print(sub.groupby(["State", "Gender"]).sum())
    print(sub.groupby(["State", "Gender"]).sum().info())

    # Step 5. Filtering with one condition
    girls = baby_names.loc[baby_names["Gender"] == "F", ["State", ]]
    print(girls.groupby("State").value_counts())

    # Step 6. Filtering with Regex
    regex = "[A-Z]e.*"
    with_j = baby_names[baby_names["Name"].str.match(regex)]
    print(with_j.sample(5))
    print(with_j.shape)

    # Step 7. Filtering with multiple conditions
    with_j = baby_names.loc[(baby_names["Name"].str.match(regex)) & (baby_names["State"] == "WA")]
    print(with_j.head(5))
    print(with_j.shape)


if __name__ == "__main__":
    main()
