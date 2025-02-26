import numpy as np
import pandas as pd
def fs_name(name,age):
    return f"My name is {name} and I am {age} years old"
def np_1(b):
    a = [1,2,3,4,5,6,7,8,9,10]
    if b<np.mean(a):
        return "The number is less than the average"
    else:
        return "The number is greater than the average"
s=fs_name("John",25)
f=np_1(11)
print(s)
print(f)