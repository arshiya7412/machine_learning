import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.DataFrame({
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [40, 45, 50, 55, 65, 70, 85, 95]
})
plt.scatter(df["Hours_Studied"], df["Marks"])
plt.xlabel("Hours_Studied")
plt.ylabel("Marks")
plt.title("Hours_studied vs Marks")
plt.show()
plt.plot(df["Hours_Studied"], df["Marks"])
plt.xlabel("Hours_Studied")
plt.ylabel("Marks")
plt.title("Hours_Studied vs Marks")
plt.show()
sns.boxplot(x=df["Marks"])
plt.title("Marks Outliers")
plt.show()
plt.hist(df["Marks"], bins  = 5)
plt.xlabel("Marks")
plt.title("Marks Distribution")
plt.show()
