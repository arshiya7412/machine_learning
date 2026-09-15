import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Income": [15, 16, 17, 50, 55, 60, 90, 95, 100],
    "Spending_Score": [80, 78, 82, 50, 48, 52, 20, 18, 15]
})

X = df[["Income", "Spending_Score"]]

kmeans = KMeans(n_clusters = 2, random_state = 42)
df["Clusters"] = kmeans.fit_predict(X)

print(df)
print("Clusters are:", kmeans.cluster_centers_)

plt.scatter(df["Income"], df["Spending_Score"], c = df["Clusters"])
plt.scatter(kmeans.cluster_centers_[:,0],
            kmeans.cluster_centers_[:,1],
            marker = "X")
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("K-Means Clustering")
plt.show()
