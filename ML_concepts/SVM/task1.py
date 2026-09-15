from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd

df = pd.DataFrame({
    "Hours": [1,2,3,4,5,6,7,8],
    "Marks": [35,40,45,55,65,70,80,90],
    "Passed": [0,0,0,0,1,1,1,1]
})

X = df[["Hours", "Marks"]]
y = df["Passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = SVC(kernel="linear")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
