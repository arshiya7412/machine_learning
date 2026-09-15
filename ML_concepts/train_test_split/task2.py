from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.DataFrame({
    "Experience_Years": [0.5, 1, 2, 3, 4, 5, 6, 7],
    "Salary_LPA": [2, 3, 4, 6, 7, 9, 11, 13]
})
X = df[["Experience_Years"]]
y = df["Salary_LPA"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)
print(X_train)
print(X_test)
print(df.shape)
