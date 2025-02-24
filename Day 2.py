import numpy as np 
import pandas as pd 
average = [1,2,3,4,5,6,7,8,9,10]
b = np.mean(average)
print(f'Average of the list is {b}')
data = {'Name': ["Smith","Kat"] , 'age': [25,35]}
c = pd.DataFrame(data)
print(c)