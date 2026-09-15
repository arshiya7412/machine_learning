import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.DataFrame({
    "Study_Hours": [2, 4, 6, 8, 10, 5, 7],
    "Attendance": [60, 70, 80, 90, 95, 75, 85],
    "Passed": [0, 0, 1, 1, 1, 1, 1]
})

X = df[["Study_Hours", "Attendance"]]
y = df["Passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = DecisionTreeClassifier(
    max_depth=10,
    random_state=42
)
model.fit(X_train, y_train)
