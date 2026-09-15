import pandas as pd
data = {
    "Name": ["Alice", "Anderson", "Joyce"],
    "Age": [25, 30, 35],
    "Score": [7, 8, 9]
    }

df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.info())
print(df.describe())
print(df["Age"])
print(df.iloc[1])
