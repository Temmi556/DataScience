import numpy as np
import pandas as pd

# Sales data
sales = {
    "Product": ["Apples", "Pears", "Bananas"],
    "Price": [20, 30, 15],
    "Quantity": [50, 30, 70]
}
df = pd.DataFrame(sales)

# Analysis
total_sales = df["Quantity"].sum()
average_price = np.mean(df["Price"]) 
print("Sales table:")
print(df)
print(f"Total units sold: {total_sales}")
print(f"Average price: {average_price}")
