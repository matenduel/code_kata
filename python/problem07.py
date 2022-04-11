"""
Problem07: parquet 쓰고 읽기 & 이미지 포맷별 이미지 갯수 구하기

Step
1. Read parquet data
    1.1 Use pandas
    1.2 Install pyarrow to read parquet
2. Split the img field to list
    2.1 img field is a string that concatenates the path of the image with "|"
        ex) path/to/image.png|path/to/image2.jpg
3. Extract the image format
4. Count the image format
"""
import pandas as pd


def main() -> dict:
    result = {}
    file_path = "./files/product_list_with_imgs.parquet"

    # Step 1: Read parquet data

    # Step 2: Split the img field to list
    # Step 3: extract the image format
    # Step 4: count the image format

    return result


if __name__ == "__main__":
    print(main())
