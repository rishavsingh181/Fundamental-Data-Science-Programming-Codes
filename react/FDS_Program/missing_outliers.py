import pandas as pd
import numpy as np

data = {'Marks':[85,90,np.nan,95,100,30,110,np.nan,88,92]}
df = pd.DataFrame(data)

print("Original:\n", df)

# Fill missing
mean_val = df['Marks'].mean()
df['Marks'].fillna(mean_val, inplace=True)

print("\nAfter Missing Handling:\n", df)

# Remove outliers
filtered_df = df[(df['Marks']>=0) & (df['Marks']<=100)]

print("\nAfter Removing Outliers:\n", filtered_df)