data = {
    "Name": ["Alice", "Bob", None, "David", "Eve", "Bob"],
    "Age": [25, 30, 22, None, 28, 30],
    "Gender": ["Female", "Male", "Female", "Male", None, "Male"],
    "Score": [85, 90, 88, 92, 95, 90]
}
df = pd.DataFrame(data)
print(df)
df['Name'] = df['Name'].fillna('Megan')
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Gender'] = df['Gender'].fillna('Unknown')
df = df.drop_duplicates()
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1, 'Unknown': 2})
print(df)
