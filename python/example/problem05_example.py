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
    # Step 1: Get file path in data directory
    file_path_list = glob("../data/*.txt")

    # Step 2: Make Regex expression
    email_extractor = re.compile("(?P<email>[a-zA-z0-9-]+@[a-zA-z0-9-]+.(co.kr|com|kr))")

    # Step 3: Read the file with for loop
    result = set([])
    for file_path in file_path_list:
        with open(file_path, "r", encoding="utf-8") as f:
            # Step 4: Extract the email from the txt file
            email_list = email_extractor.finditer(f.read())
            for email in email_list:
                result.add(email.group("email"))

    # Step 5: Return the email without duplicate
    return result


if __name__ == "__main__":
    print(extract_email_from_txt())
