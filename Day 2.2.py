import pandas as pd
adas = {
    "Products": ["Milk", "Bread", "Eggs", "Cheese"],
    "Price": [50, 30, 100, 80],
    "Quantity": [2, 3, 1, 4],
    "Total": [100, 90, 100, 320]
}
print(pd.DataFrame(adas))