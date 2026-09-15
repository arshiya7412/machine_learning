import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.DataFrame({
     "Hours_studied" :[1, 2, 3, 8, 9, 10],
     "Marks" :[40, 42, 45, 85, 88, 90]
})

X = df[["Hours_studied", "Marks"]]

model = KMeans(n_clusters = 3, random_state = 42)
df["Clusters"] = model.fit_predict(X)

print(df)
print("Cluster Centers:")
print(model.cluster_centers_)
plt.scatter(df["Hours_studied"], df["Marks"], c = df["Clusters"])
plt.scatter(model.cluster_centers_[:,0],
            model.cluster_centers_[:,1],
            marker = "X")

plt.xlabel("Hours_studied")
plt.ylabel("Marks")
plt.title("K-Means Clustering")
plt.show()
