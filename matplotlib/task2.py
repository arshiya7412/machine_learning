import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [40, 45, 50, 55, 65, 70, 85, 95]
})
print(df)
print(df.describe())
print(df.corr())
sns.heatmap(df.corr(), annot=True, cmap = "YlGnBu")
plt.show()
