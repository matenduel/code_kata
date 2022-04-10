"""
Problem05: Extract the all email address from txt file in certain directory

Step
1. Get file path in data directory
    1.1 All files are located in data directory
2. Make Regex expression
    2.1 ID part of email are consist of the alphabet(upper, lower) and numeric and '-'
3. Read the file with for loop
4. Extract the email from the txt file
5. Return the email without duplicate
"""
import re
from glob import glob


def extract_email_from_txt() -> set[str]:
    pass


if __name__ == "__main__":
    print(extract_email_from_txt())


