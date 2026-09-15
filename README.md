# Machine Learning
 
A hands-on collection of machine learning exercises covering the core Python data-science stack (NumPy, pandas, Matplotlib/Seaborn) and classic ML algorithms, implemented and worked through in small, focused scripts.
 
## 📂 Repository Structure
 
```
machine_learning/
├── numpy_ML/          # NumPy fundamentals for ML
├── pandas/            # Data handling & cleaning with pandas
├── matplotlib/        # Data visualization
└── ML_concepts/        # Core ML algorithms with scikit-learn
    ├── Linear_Regression/
    ├── Decision_tree/
    ├── SVM/
    ├── KMeans/
    ├── naive_bayes/
    ├── train_test_split/
    ├── knn.py
    ├── pca.py
    └── random_forest_&_logistic_regression.py
```
 
## 🧠 What's Inside
 
### `numpy_ML/`
Array basics used throughout ML: shapes, `mean`/`sum`/`max`, variance, and broadcasting.
 
### `pandas/`
Building and inspecting DataFrames, indexing/filtering rows, handling missing values (`fillna`, `dropna`), removing duplicates, encoding categorical columns, and loading data from CSV.
 
### `matplotlib/`
Visualizing data with scatter plots, line plots, box plots, histograms, and Seaborn heatmaps (including correlation matrices) — mostly on small "hours studied vs marks" style datasets.
 
### `ML_concepts/`
Classic supervised and unsupervised learning algorithms, each demoed on a small toy dataset:
 
- **Linear Regression** — gradient descent implemented from scratch (NumPy), plus scikit-learn's `LinearRegression` with MSE/R² evaluation
- **Decision Tree** — classification with `DecisionTreeClassifier`, including a `max_depth` tuning example
- **K-Nearest Neighbors (KNN)** — classification with `KNeighborsClassifier`
- **Support Vector Machine (SVM)** — linear and RBF kernels compared on accuracy/confusion matrix
- **Naive Bayes** — `GaussianNB` for classification
- **K-Means** — unsupervised clustering with visualized cluster centers
- **PCA** — dimensionality reduction with `StandardScaler` + `PCA`, explained variance ratio
- **Random Forest & Logistic Regression** — compared side by side on the same dataset
- **Train/Test Split** — splitting data correctly before model training
## 🛠️ Tools & Libraries
- Python
- NumPy
- pandas
- Matplotlib & Seaborn
- scikit-learn
## 🎯 Purpose
This repo documents my progression through core ML concepts — from raw data manipulation to training and evaluating models — as part of building a practical foundation in machine learning.
 
