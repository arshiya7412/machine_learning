data = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Megan"],
    "Math": [85, 90, 78, 92, 88],
    "Physics": [92, 88, 95, 89, 91],
    "Chemistry": [72, 80, 78, 85, 76]
}

df = pd.DataFrame(data)
print(df)
print(df.iloc[0:3])
print(df.describe())
print(df[df["Math"] > 80])
data["Total"] = df["Math"] + df["Physics"] + df["Chemistry"]
df = pd.DataFrame(data)
print(df)
