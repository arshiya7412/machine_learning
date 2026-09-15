import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.DataFrame({
    "Hours_Studied": [1,2,3,4,5,6,7,8,9,10],
    "Attendance": [90,85,80,75,70,65,60,55,50,45],
    "Passed": [1,1,1,1,0,0,0,0,0,0]
})

X = df[["Hours_Studied", "Attendance"]]
y = df["Passed"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

model = SVC(kernel="linear")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Prediction for student:\n", model.predict([[6, 70]]))


model = SVC(kernel="rbf")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy for rbf:", accuracy_score(y_test, y_pred))
print("Confusion matrix for rbf:", confusion_matrix(y_test, y_pred))
print("Prediction for student:", model.predict([[6, 70]]))
print(df)
