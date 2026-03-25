import numpy as np
import pandas as pd

# List
marks = [85, 90, 78, 88]
print("List:", marks)

# Array
arr = np.array([1,2,3,4,5])
print("Array:", arr)

# DataFrame
data = {'Name':['Ram','Sita','Ravi'], 'Marks':[85,92,78]}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Matrix
matrix = np.array([[1,2],[3,4]])
print("Matrix:\n", matrix)