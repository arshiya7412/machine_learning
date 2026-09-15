import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.DataFrame({
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [40, 45, 50, 55, 65, 70, 85, 95]
})
print(df)
X = df["Hours_Studied"]
y = df["Marks"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
print(X_train)
print(X_test)
print(df.shape)
