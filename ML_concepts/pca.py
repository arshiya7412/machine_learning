import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.DataFrame({
    "Math": [80, 85, 90, 70, 60],
    "Science": [78, 88, 92, 68, 65],
    "English": [75, 82, 88, 72, 70]
})

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

pca = PCA(n_components = 2)
x_pca = pca.fit_transform(X_scaled)
print("Transformed data:")
print(x_pca)

print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)
