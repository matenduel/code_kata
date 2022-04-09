"""
Problem04: Type check for the input data

Step
1. Make Pydantic model
    1.1 fields = ["shop_id", "revenue", "shop_name"]
2. Transform the given data
    2.1 Use Pydantic model that create in step 1
    2.2 shop_id and revenue must be integer type
3. Get total_revenue by using map function
"""

from pydantic import BaseModel


# Step 1: Make Pydantic model
class ShopInfo(BaseModel):
    pass


def get_total_revenue() -> int:
    total_revenue = 0
    datas = [
        {"shop_id": 1, "revenue": "20000", "shop_name": "Tony", "address": "dongdaemun"},
        {"shop_id": "2", "revenue": 52000, "shop_name": "Bruna Rosso"},
        {"shop_id": 3, "revenue": "187000", "address": "gang-nam"},
    ]

    # Step 2: Transform the given data

    # Step 3: Get total_revenue by using map function

    return total_revenue


if __name__ == "__main__":
    print(get_total_revenue())
