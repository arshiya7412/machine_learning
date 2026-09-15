import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.DataFrame({
    "Study_Hours" : [2, 4, 6, 8, 10],
    "Attendance" : [60, 70, 80, 90, 95],
    "Passed" : [0, 0, 1, 1, 1]
})
print(df)

X = df[['Study_Hours']]
y = df['Attendance']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:", confusion_matrix(y_test, y_pred))
print("Prediction:", model.predict([[7]]))
print("Prediction:", model.predict([[85]]))
