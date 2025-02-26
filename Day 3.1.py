import pandas as pd
import numpy as np
def average_value(data, column):
    return np.mean(data[column])
data = pd.DataFrame({
    "Product": ["Bread", "Milk", "Apples", "Bananas", "Eggs"],
    "Price": [30, 50, 20, 40, 10]
})

print(average_value(data, "Price"),"$")