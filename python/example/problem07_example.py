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
from memory_profiler import profile


@profile
def main() -> dict:
    result = {}
    file_path = "../files/product_list_with_imgs.parquet"

    # Step 1: Read parquet data
    product_datas = pd.read_parquet(file_path)

    # Step 2: Split the img field to list
    for images in product_datas["img"]:
        for image in images.split("|"):
            # Step 3: extract the image format
            path_and_file_name, ext = image.rsplit(".", 1)
            # Step 4: count the image format
            if ext not in result:
                result[ext] = 1
            else:
                result[ext] += 1

    return result


if __name__ == "__main__":
    print(main())
