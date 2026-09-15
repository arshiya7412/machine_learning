import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.DataFrame({
    "Age": [18, 20, 22, 24, 26, 28, 30],
    "Score": [65, 70, 75, 80, 85, 90, 95]
})
print(df)
plt.plot(df["Age"], df["Score"])
plt.xlabel("Age")
plt.ylabel("Score")
plt.title("Age vs Score")
plt.show()
plt.scatter(df["Age"], df["Score"])
plt.xlabel("Age")
plt.ylabel("Score")
plt.title("Age vs Score (Scatter)")
plt.show()
sns.boxplot(x=df["Score"])
plt.title("Score Outliers")
plt.show()
plt.hist(df["Score"], bins=5)
plt.xlabel("Score")
plt.title("Score Distribution")
plt.show()
