    MACHINE LEARNING LAB
LABORATORY MANUAL VII Semester
(Academic Year: 2025-26)
  DEPARTMENT OF AIML
Atria Institute of Technology Bengaluru – 560 024
  
   LIST OF EXPERIMENTS
   Develop a program to Load a dataset and select one numerical column. Compute mean, median, mode, standard deviation, variance, and range for a given numerical column in a dataset. Generate a histogram and boxplot to understand the distribution of the data. Identify any outliers in the data using IQR. Select a categorical variable from a dataset. Compute the frequency of each category and display it as a bar chart or pie chart.
   Develop a program to Load a dataset with at least two numerical columns (e.g., Iris, Titanic). Plot a scatter plot of two variables and calculate their Pearson correlation coefficient. Write a
program to compute the covariance and correlation matrix for a dataset. Visualize the correlation matrix using a heatmap to know which variables have strong positive/negative correlations.
  1
2
 3 Develop a program to implement Principal Component Analysis (PCA) for reducing the dimensionality of the Iris dataset from 4 features to 2.
4
5 NA
6 Implement the non-parametric Locally Weighted Regression algorithm in order to
fit data points. Select appropriate data set for your experiment and draw graphs.
7
8 Develop a program to load the Titanic dataset. Split the data into training and test sets. Train a decision tree classifier. Visualize the tree structure. Evaluate accuracy, precision, recall, and F1-score.
9 Develop a program to implement the Naive Bayesian classifier considering Iris dataset for training. Compute the accuracy of the classifier, considering the test data.
10 Develop a program to implement k-means clustering using Wisconsin Breast
Cancer data set and visualize the clustering result.
DEPARTMENT OF AIML
Atria Institute of Technology Bengaluru – 560 024
   Develop a program to load the Iris dataset. Implement the k-Nearest Neighbors (k- NN) algorithm for classifying flowers based on their features. Split the dataset into training and testing sets and evaluate the model using metrics like accuracy and F1- score. Test it for different values of 𝑘 (e.g., k=1,3,5) and evaluate the accuracy. Extend the k-NN algorithm to assign weights based on the distance of neighbors (e.g., 𝑤𝑒𝑖𝑔h𝑡=1/𝑑2 ). Compare the performance of weighted k-NN and regular k- NN on a synthetic or real-world dataset.
      Develop a program to demonstrate the working of Linear Regression and Polynomial Regression. Use Boston Housing Dataset for Linear Regression and Auto MPG Dataset (for vehicle fuel efficiency prediction) for Polynomial Regression.
       
BCS606 Machine Learning Lab 1
 1 Experiment 1: Descriptive Statistics & Data Visualization
Develop a program to Load a dataset and select one numerical column. Compute mean, median, mode, standard deviation, variance, and range for a given numer- ical column in a dataset. Generate a histogram and boxplot to understand the distribution of the data. Identify any outliers in the data using IQR. Select a categorical variable from a dataset. Compute the frequency of each category and display it as a bar chart or pie chart.
1.1 Aim
To compute central tendency, dispersion, and visualize distributions and outliers.
1.2 Procedure:
1. Load the dataset (Iris) using Pandas.
2. Select a numerical column and calculate Mean, Median, Mode, Std Dev, and Range.
3. Use the IQR method (Q3 - Q1) to identify potential outliers.
4. Plot a Histogram and Boxplot using Seaborn.
5. Create a Pie/Bar chart for categorical frequency distribution.
1.3 Code:
import pandas as pd
import seaborn as sns
Computer Science and Engineering
1 of 33
 
BCS606 Machine Learning Lab 2
 import matplotlib.pyplot as plt
import pprint
# Load Dataset
#df = sns.load_dataset('iris')
df = pd.read_csv('datasets/iris.csv')
col = 'sepal_length'
print('R E S U L T S:') # 1. Statistics
stats = {
    "Mean"    : round(df[col].mean(),2),
    "Median"  : round(df[col].median(), 2),
    "Mode"    : round(df[col].mode()[0], 2),
    "Std Dev" : round(df[col].std(), 2),
    "Variance": round(df[col].var(), 2),
    "Range"   : round(df[col].max() - df[col].min(), 2)
}
print("Statistics:")
pprint.pprint(stats)
# 2. Outlier Detection (IQR)
Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))] print(f"\nOutliers detected: {len(outliers)}")
# 3. Visualization
plt.figure(figsize=(12, 3))
plt.subplot(1, 3, 1); sns.histplot(df[col], kde=True); plt.title("Histogram") plt.subplot(1, 3, 2); sns.boxplot(y=df[col]); plt.title("Boxplot") plt.subplot(1, 3, 3); df['species'].value_counts().plot(kind='pie',
autopct='%1.1f%%'); plt.title("Category Frequency")
print('Visualization')
plt.savefig('1.png')
plt.show()
Computer Science and Engineering 2 of 33
 
BCS606 Machine Learning Lab
3
 R E S U L T S:
Statistics:
{'Mean': np.float64(5.84),
 'Median': 5.8,
 'Mode': np.float64(5.0),
 'Range': 3.6,
 'Std Dev': 0.83,
 'Variance': 0.69}
Outliers detected: 0
Visualization
  Computer Science and Engineering
3 of 33

BCS606 Machine Learning Lab 4
 2 EXPERIMENT 2: Correlation Analysis
Develop a program to Load a dataset with at least two numerical columns (e.g., Iris, Titanic). Plot a scatter plot of two variables and calculate their Pearson correlation coefficient. Write a program to compute the covariance and correlation matrix for a dataset. Visualize the correlation matrix using a heatmap to know which variables have strong positive/negative correlations.
2.1 Aim
To analyze relationships between variables using Correlation and Heat maps. Ref 1
2.2 Procedure:
1. Load a multi-column dataset.
2. Generate a scatter plot to observe trends.
3. Calculate the Pearson Correlation Coefficient and Covariance matrix. 4. Visualize the correlation matrix using a Seaborn Heatmap.
2.3 Code
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
Computer Science and Engineering
4 of 33
 
BCS606 Machine Learning Lab 5
 print('R E S U L T S:')
# 1. Load the dataset
# We'll use Iris because it's a gold mine for numerical correlations #df = sns.load_dataset('iris')
df = pd.read_csv('datasets/iris.csv')
# 2. Scatter Plot of two variables
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x='petal_length', y='petal_width', hue='species',
                palette='viridis')
plt.title('Petal Length vs Petal Width')
# 3. Calculate Pearson Correlation Coefficient
# We'll compute it specifically for the two variables in the scatter plot pearson_corr = df['petal_length'].corr(df['petal_width'])
print(f"Pearson Correlation (Petal Length vs Width): {pearson_corr:.4f}")
# 4. Compute Covariance and Correlation Matrices
# We only select numerical columns to avoid errors with categorical data numerical_df = df.select_dtypes(include=['float64', 'int64'])
cov_matrix = numerical_df.cov()
corr_matrix = numerical_df.corr()
print("\n--- Covariance Matrix ---") print(cov_matrix)
print("\n--- Correlation Matrix ---") print(corr_matrix)
# 5. Visualize the Correlation Matrix using a Heatmap
plt.subplot(1, 2, 2)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5) plt.title('Correlation Matrix Heatmap')
plt.tight_layout()
print('Visualization')
plt.savefig('2.png')
plt.show()
Computer Science and Engineering
5 of 33
 
BCS606 Machine Learning Lab 6
 R E S U L T S:
Pearson Correlation (Petal Length vs Width): 0.9629
--- Covariance Matrix ---
              sepal_length  sepal_width  petal_length  petal_width
sepal_length      0.685694
sepal_width      -0.042434
petal_length      1.274315
petal_width       0.516271
-0.042434
 0.189979
-0.329656
-0.121639
 1.274315
-0.329656
 3.116278
 1.295609
 0.516271
-0.121639
 1.295609
 0.581006
--- Correlation Matrix ---
              sepal_length  sepal_width  petal_length  petal_width
sepal_length      1.000000
sepal_width      -0.117570
petal_length      0.871754
petal_width       0.817941
Visualization
-0.117570
 1.000000
-0.428440
-0.366126
 0.871754
-0.428440
 1.000000
 0.962865
 0.817941
-0.366126
 0.962865
 1.000000
  Computer Science and Engineering
6 of 33

BCS606 Machine Learning Lab 7
 3 EXPERIMENT 3: Principal Component Analysis (PCA)
Develop a program to implement Principal Component Analysis (PCA) for reduc- ing the dimensionality of the Iris dataset from 4 features to 2.
3.1 Aim
Dimensionality reduction of the Iris dataset.
3.2 Procedure:
1. Load Iris features (4D).
2. Apply PCA to transform 4 features into 2 Principal Components.
3. Plot the resulting components to visualize how much variance is retained
3.3 Code
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler from sklearn.decomposition import PCA
print('R E S U L T S:')
# 1. Load the Iris dataset
#iris = load_iris()
#X = iris.data
Computer Science and Engineering
7 of 33
 
BCS606 Machine Learning Lab 8
 #y = iris.target
#feature_names = iris.feature_names
#target_names = iris.target_names
df = pd.read_csv('datasets/iris.csv')
X = df.drop('species', axis=1)
y = df['species']
feature_names = df.columns[:-1].tolist()
target_names = df['species'].unique()
print(f"Original shape: {X.shape} (4 features)")
# 2. Standardize the data (Mean = 0, Variance = 1) # PCA is affected by scale, so this step is crucial X_scaled = StandardScaler().fit_transform(X)
# 3. Implement PCA to reduce from 4 features to 2
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X_scaled)
# 4. Create a DataFrame for visualization
pca_df = pd.DataFrame(data=principal_components, columns=['Principal Component 1', 'Principal Com pca_df['target'] = y
#pca_df['species'] = pca_df['target'].map({i: name for i, name in enumerate(target_names)}) pca_df['species'] = y
print(f"Reduced shape: {principal_components.shape} (2 features)")
# 5. Calculate Explained Variance
variance_ratio = pca.explained_variance_ratio_
print(f"\nExplained Variance Ratio: {variance_ratio}") print(f"Total Variance Retained: {sum(variance_ratio) * 100:.2f}%")
# 6. Visualize the results
plt.figure(figsize=(10, 7))
sns.scatterplot(x='Principal Component 1', y='Principal Component 2',
                hue='species', data=pca_df, s=100, palette='viridis')
plt.title('PCA of Iris Dataset (4D to 2D Reduction)', fontsize=15)
Computer Science and Engineering
8 of 33
 
BCS606 Machine Learning Lab
9
 plt.xlabel(f'PC1 ({variance_ratio[0]*100:.1f}% Variance)') plt.ylabel(f'PC2 ({variance_ratio[1]*100:.1f}% Variance)') plt.grid(True, linestyle='--', alpha=0.6)
print('Visualization')
plt.savefig('3.png')
plt.show()
R E S U L T S:
Original shape: (150, 4) (4 features)
Reduced shape: (150, 2) (2 features)
Explained Variance Ratio: [0.72962445 0.22850762]
Total Variance Retained: 95.81%
Visualization
  Computer Science and Engineering
9 of 33

BCS606 Machine Learning Lab 10
 4 EXPERIMENT 4: k-Nearest Neighbors (k-NN)
Develop a program to load the Iris dataset. Implement the k-Nearest Neighbors (k- NN) algorithm for classifying flowers based on their features. Split the dataset into training and testing sets and evaluate the model using metrics like accuracy and F1-score. Test it for different values of (e.g., k=1,3,5) and evaluate the accuracy. Extend the k-NN algorithm to assign weights based on the distance of neighbors (e.g., =1/2 ). Compare the performance of weighted k-NN and regular k-NN on a synthetic or real-world dataset.
4.1 Aim
Classify flowers and compare Regular vs. Weighted k-NN.
4.2 Procedure:
1. Split Iris data into Training (80%) and Testing (20%) sets.
2. Train a k-NN classifier for k=1, 3, and 5.
3. Implement Weighted k-NN using the inverse distance formula (w = 1/d2). 4. Compare Accuracy and F1-Scores.
4.3 Code
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
Computer Science and Engineering
10 of 33
 
BCS606 Machine Learning Lab 11
 from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
print('R E S U L T S:')
# 1. Load the Iris dataset
#iris = load_iris()
#X, y = iris.data, iris.target
#target_names = iris.target_names
df = pd.read_csv('datasets/iris.csv')
X = df.drop('species', axis=1)
y = df['species']
target_names = df['species'].unique()
# 2. Split into Training and Testing sets (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# 3. Define a custom weight function for w = 1/d^2
def inverse_square_weight(distances):
# Add a small epsilon to avoid division by zero return 1 / (distances ** 2 + 1e-10)
# 4. Evaluate k-NN for different values of k
k_values = [1, 3, 5]
results = []
for k in k_values:
# --- Regular k-NN (Uniform weights) ---
knn_reg = KNeighborsClassifier(n_neighbors=k, weights='uniform') knn_reg.fit(X_train, y_train)
y_pred_reg = knn_reg.predict(X_test)
    acc_reg = accuracy_score(y_test, y_pred_reg)
    f1_reg = f1_score(y_test, y_pred_reg, average='weighted')
Computer Science and Engineering
11 of 33
 
BCS606 Machine Learning Lab 12
     # --- Weighted k-NN (Custom weights: 1/d^2) ---
    knn_weight = KNeighborsClassifier(n_neighbors=k, weights=inverse_square_weight)
    knn_weight.fit(X_train, y_train)
    y_pred_weight = knn_weight.predict(X_test)
    acc_weight = accuracy_score(y_test, y_pred_weight)
    f1_weight = f1_score(y_test, y_pred_weight, average='weighted')
    results.append({
        'k': k,
        'Reg_Acc': acc_reg,
        'Reg_F1': f1_reg,
        'Weight_Acc': acc_weight,
        'Weight_F1': f1_weight
})
# 5. Display Results
res_df = pd.DataFrame(results) print("Performance Comparison:") print(res_df.to_string(index=False))
# Detailed report for the best k (e.g., k=3)
print("\nDetailed Classification Report (Weighted k=3):")
best_knn = KNeighborsClassifier(n_neighbors=3, weights=inverse_square_weight) best_knn.fit(X_train, y_train)
print(classification_report(y_test, best_knn.predict(X_test), target_names=target_names))
R E S U L T S:
Performance Comparison:
 k  Reg_Acc  Reg_F1  Weight_Acc  Weight_F1
1      1.0     1.0
3      1.0     1.0
5      1.0     1.0
1.0        1.0
1.0        1.0
1.0        1.0
Detailed Classification Report (Weighted k=3):
              precision    recall  f1-score   support
Computer Science and Engineering
12 of 33
 
BCS606
Machine Learning Lab
13
       setosa
  versicolor
   virginica
    accuracy
   macro avg
weighted avg
1.00      1.00
1.00      1.00
1.00      1.00
1.00      1.00
1.00      1.00
1.00        10
1.00         9
1.00        11
1.00        30
1.00        30
1.00        30
 Computer Science and Engineering
13 of 33

BCS606 Machine Learning Lab 14
 5 EXPERIMENT 5: MISSING
 Computer Science and Engineering 14 of 33

BCS606 Machine Learning Lab 15
 6 EXPERIMENT 6: Locally Weighted Regression (LWR)
Implement the non-parametric Locally Weighted Regression algorithm in order to fit data points. Select appropriate data set for your experiment and draw graphs.
6.1 Aim
To fit data points using a non-parametric regression approach.
6.2 Procedure:
1. Define a Gaussian Kernel function to assign weights. 2. For every test point, calculate a local weight matrix. 3. Fit a local regression line and plot the non-linear fit.
6.3 Code
import numpy as np
import matplotlib.pyplot as plt
print('R E S U L T S:')
np.random.seed(42)
X = np.linspace(-3, 3, 100).reshape(-1, 1)
y = np.sin(X).ravel() + np.random.normal(scale=0.1, size=X.shape[0])
def locally_weighted_regression(x_query, X_train, y_train, tau): W = np.exp(-((X_train - x_query) ** 2) / (2 * tau ** 2)) X_bias = np.c_[np.ones_like(X_train), X_train]
Computer Science and Engineering
15 of 33
 
BCS606 Machine Learning Lab 16
     theta = np.linalg.pinv(X_bias.T @ np.diag(W.ravel()) @ X_bias) @ X_bias.T @ \
            np.diag(W.ravel()) @ y_train
return np.array([1, x_query]) @ theta # Predict y for x_query X_test = np.linspace(-3, 3, 100)
y_pred = np.array([locally_weighted_regression(x, X, y, tau=0.5) for x in X_test])
plt.scatter(X, y, color="gray", alpha=0.5, label="Training Data")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="LWR Fit (=0.5)")
plt.legend()
print('Visualization')
plt.savefig('6.png')
plt.show()
R E S U L T S:
Visualization
 Computer Science and Engineering
16 of 33

BCS606 Machine Learning Lab 17
   Computer Science and Engineering 17 of 33

BCS606 Machine Learning Lab 18
 7 EXPERIMENT 7: Linear & Polynomial Regression
Develop a program to demonstrate the working of Linear Regression and Polyno- mial Regression. Use California Housing Dataset for Linear Regression and Auto MPG Dataset (for vehicle fuel efficiency prediction) for Polynomial Regression.
7.1 Aim
To fit data points using a non-parametric regression approach.
7.2 Procedure:
1. Implement Linear Regression for the California Housing context.
2. Use PolynomialFeatures to transform data for the Auto MPG dataset. 3. Evaluate using Mean Squared Error and visualize the curves.
7.3 Code
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures from sklearn.model_selection import train_test_split from sklearn.metrics import mean_squared_error, r2_score
print('R E S U L T S:')
Computer Science and Engineering
18 of 33
 
BCS606 Machine Learning Lab 19
 # --- 1. Linear Regression (California Housing) ---
print("--- Part 1: Linear Regression (California Housing) ---") #california = fetch_california_housing()
df = pd.read_csv('datasets/california_housing.csv')
# Use 'MedInc' (Median Income) as it has the strongest linear
# correlation with price
#X = california.data[:, 0].reshape(-1, 1)
#y = california.target
X = df[['MedInc']].values # Using double brackets [[ ]] is a shortcut for reshape(-1, 1) y = df['MedHouseVal'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                        random_state=42)
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred_lin = lin_reg.predict(X_test)
print(f"Linear R2 Score: {r2_score(y_test, y_pred_lin):.4f}") print(f"Linear MSE: {mean_squared_error(y_test, y_pred_lin):.4f}")
# --- 2. Polynomial Regression (Auto MPG) ---
print("\n--- Part 2: Polynomial Regression (Auto MPG) ---") # Loading from Seaborn's built-in datasets
df_mpg = sns.load_dataset('mpg').dropna()
# Using 'horsepower' to predict 'mpg' (Relationship is non-linear)
X_hp = df_mpg[['horsepower']]
y_mpg = df_mpg['mpg']
X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(X_hp, y_mpg,
                                  test_size=0.2, random_state=42)
# Transform features to Polynomial (Degree 2)
poly_features = PolynomialFeatures(degree=2)
X_train_poly = poly_features.fit_transform(X_train_p)
X_test_poly = poly_features.transform(X_test_p)
Computer Science and Engineering
19 of 33
 
BCS606 Machine Learning Lab 20
 poly_reg = LinearRegression()
poly_reg.fit(X_train_poly, y_train_p)
y_pred_poly = poly_reg.predict(X_test_poly)
print(f"Polynomial R2 Score: {r2_score(y_test_p, y_pred_poly):.4f}") print(f"Polynomial MSE: {mean_squared_error(y_test_p, y_pred_poly):.4f}")
# --- 3. Visualization ---
plt.figure(figsize=(14, 5))
# Plot Linear Regression Result
plt.subplot(1, 2, 1)
plt.scatter(X_test, y_test, color='teal', alpha=0.3, label='Actual Data')
plt.plot(X_test, y_pred_lin, color='red', linewidth=2, label='Linear Fit')
plt.title("California Housing: Price vs Median Income")
plt.xlabel("Median Income")
plt.ylabel("House Value ($100k)")
plt.legend()
# Plot Polynomial Regression Result
plt.subplot(1, 2, 2)
plt.scatter(X_test_p, y_test_p, color='purple', alpha=0.4, label='Actual Data') # Sorting values for a smooth curve plot
sort_idx = np.argsort(X_test_p.values.flatten()) plt.plot(X_test_p.values[sort_idx], y_pred_poly[sort_idx], color='gold',
         linewidth=3, label='Polynomial Fit (Deg 2)')
plt.title("Auto MPG: MPG vs Horsepower")
plt.xlabel("Horsepower")
plt.ylabel("Miles Per Gallon (MPG)")
plt.legend()
plt.tight_layout()
print('Visualization')
plt.savefig('6.png')
plt.show()
R E S U L T S:
--- Part 1: Linear Regression (California Housing) ---
Computer Science and Engineering
20 of 33
 
BCS606 Machine Learning Lab
21
 Linear R2 Score: 0.4589
Linear MSE: 0.7091
--- Part 2: Polynomial Regression (Auto MPG) ---
Polynomial R2 Score: 0.6392
Polynomial MSE: 18.4170
Visualization
  Computer Science and Engineering
21 of 33

BCS606 Machine Learning Lab 22
 8 EXPERIMENT 8: Decision Tree (Titanic)
Develop a program to load the Titanic dataset. Split the data into training and test sets. Train a decision tree classifier. Visualize the tree structure. Evaluate accuracy, precision, recall, and F1-score.
8.1 Aim
Predict survival on the Titanic and visualize the tree structure.
8.2 Procedure:
1. Preprocess Titanic data (handle missing values, encode gender). 2. Train a DecisionTreeClassifier.
3. Export and plot the tree structure to understand decision nodes. 4. Compute Precision, Recall, and F1-score.
8.3 Code
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree from sklearn.metrics import accuracy_score, precision_score, \
     recall_score, f1_score, confusion_matrix
print('R E S U L T S:')
Computer Science and Engineering
22 of 33
 
BCS606 Machine Learning Lab 23
 # 1. Load Dataset
# We use seaborn to load the titanic dataset easily # df = sns.load_dataset('itanic')
df = pd.read_csv('datasets/titanic.csv')
# 2. Preprocessing
# Select relevant features for prediction
# 'pclass': Ticket class, 'sex': Gender, 'age': Age, 'fare': Ticket fare features = ['pclass', 'sex', 'age', 'fare']
target = 'survived'
# Drop rows with missing values (Decision Trees in sklearn don't handle
# NaNs natively)
df = df[features + [target]].dropna()
# Encode 'sex' column (Male=0, Female=1)
df['sex'] = df['sex'].map({'male': 0, 'female': 1})
# Separate X (features) and y (target)
X = df[features]
y = df[target]
# 3. Split Data into Training and Testing Sets (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                               random_state=42)
# 4. Train Decision Tree Classifier
# We limit max_depth=3 to make the visualization readable and avoid overfitting clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42) clf.fit(X_train, y_train)
# 5. Make Predictions
y_pred = clf.predict(X_test)
# 6. Evaluate the Model
print("--- Model Performance Metrics ---") print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}") print(f"Precision: {precision_score(y_test, y_pred):.4f}")
Computer Science and Engineering
23 of 33
 
BCS606 Machine Learning Lab
24
 print(f"Recall: {recall_score(y_test, y_pred):.4f}") print(f"F1-Score: {f1_score(y_test, y_pred):.4f}")
print("\n--- Confusion Matrix ---") print(confusion_matrix(y_test, y_pred))
# 7. Visualize the Tree
plt.figure(figsize=(14, 8))
plot_tree(clf,
feature_names=features, class_names=['Died', 'Survived'], filled=True,
rounded=True,
          fontsize=10)
plt.title("Decision Tree Visualization (Titanic Survival Prediction)")
print('Visualization')
plt.savefig('8.png')
plt.show()
R E S U L T S:
--- Model Performance Metrics ---
Accuracy:  0.7413
Precision: 0.6939
Recall:    0.6071
F1-Score:  0.6476
--- Confusion Matrix ---
[[72 15]
 [22 34]]
Visualization
Computer Science and Engineering
24 of 33
 
BCS606 Machine Learning Lab 25
   Computer Science and Engineering 25 of 33

BCS606 Machine Learning Lab 26
 9 EXPERIMENT 9: Naive Bayesian Classifier
Develop a program to implement the Naive Bayesian classifier considering Iris dataset for training. Compute the accuracy of the classifier, considering the test data.
9.1 Aim
Implement a probabilistic classifier for the Iris dataset.
9.2 Procedure:
1. Load data and split into train/test sets.
2. Train the Gaussian Naive Bayes model.
3. Predict results for the test set and calculate the Accuracy.
9.3 Code
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
print('R E S U L T S:')
# 1. Load the Iris Dataset
Computer Science and Engineering 26 of 33
 
BCS606 Machine Learning Lab 27
 #iris = load_iris()
#X = iris.data
#y = iris.target
#target_names = iris.target_names
df = pd.read_csv('datasets/iris.csv')
X = df.drop('species', axis=1)
y = df['species']
target_names = df['species'].unique()
# 2. Split the Data into Training and Testing Sets
# 80% for Training, 20% for Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 3. Initialize and Train the Naive Bayes Classifier
# We use 'GaussianNB' because the features (sepal length, width, etc.) are continuous numerical v gnb = GaussianNB()
gnb.fit(X_train, y_train)
# 4. Make Predictions on the Test Data
y_pred = gnb.predict(X_test)
# 5. Compute and Display Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of Naive Bayes Classifier: {accuracy * 100:.2f}%")
# 6. Detailed Evaluation
print("\n--- Classification Report ---") print(classification_report(y_test, y_pred, target_names=target_names))
print("--- Confusion Matrix ---")
cm = confusion_matrix(y_test, y_pred)
print(cm)
# 7. Visualization of Results (Optional)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=target_names,
            yticklabels=target_names)
plt.title('Confusion Matrix: Naive Bayes')
plt.xlabel('Predicted')
Computer Science and Engineering 27 of 33
 
BCS606 Machine Learning Lab
28
 plt.ylabel('Actual')
print('Visualization')
plt.savefig('9.png')
plt.show()
R E S U L T S:
Accuracy of Naive Bayes Classifier: 100.00%
--- Classification Report ---
              precision    recall
f1-score   support
    1.00        10
    1.00         9
    1.00        11
    1.00        30
    1.00        30
    1.00        30
      setosa
  versicolor
   virginica
    accuracy
   macro avg
weighted avg
1.00      1.00
1.00      1.00
1.00      1.00
1.00      1.00
1.00      1.00
--- Confusion Matrix ---
[[10  0  0]
[0 9 0]
[0 011]] Visualization
 Computer Science and Engineering
28 of 33

BCS606 Machine Learning Lab 29
   Computer Science and Engineering 29 of 33

BCS606 Machine Learning Lab 30
 10 EXPERIMENT 10: k-means Clustering
Develop a program to implement k-means clustering using Wisconsin Breast Can- cer data set and visualize the clustering result.
10.1 Aim
Unsupervised grouping of the Breast Cancer dataset.
10.2 Procedure:
1. Standardize the dataset features.
2. Apply k-means with k=2 (Malignant/Benign).
3. Visualize the clusters and identify the cluster centroids.
10.3 Code
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix, accuracy_score
print('R E S U L T S:')
Computer Science and Engineering
30 of 33
 
BCS606 Machine Learning Lab 31
 # 1. Load the Dataset
#data = load_breast_cancer()
#X = data.data
#y = data.target  # 0 = Malignant, 1 = Benign (Ground Truth)
df = pd.read_csv('datasets/breast_cancer.csv')
X = df.drop('target', axis=1)
y = df['target']
# 2. Preprocessing: Standardization
# K-means is distance-based, so scaling features is critical. scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# 3. Apply k-means Clustering
# We choose k=2 because we know there are 2 diagnosis types (Malignant/Benign) kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(X_scaled)
# 4. Dimensionality Reduction for Visualization (30D -> 2D)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
# Transform the cluster centers to 2D space for plotting
centers_pca = pca.transform(kmeans.cluster_centers_) # 5. Visualization
plt.figure(figsize=(10, 6))
# Plot the data points colored by their K-Means Cluster
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=cluster_labels, cmap='viridis',
                      alpha=0.6, edgecolors='k')
plt.scatter(centers_pca[:, 0], centers_pca[:, 1], s=300, c='red', marker='X',
            label='Centroids')
plt.title('k-means Clustering on Breast Cancer Data (PCA Reduced)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
Computer Science and Engineering
31 of 33
 
BCS606 Machine Learning Lab 32
 print('Visualization')
plt.savefig('10.png')
plt.show()
# 6. Evaluation (Comparing against Ground Truth)
# Note: K-means labels (0/1) might be swapped compared to true labels (0/1). # We check the confusion matrix to see the alignment.
print("\n--- Confusion Matrix (Clusters vs Actual) ---")
cm = confusion_matrix(y, cluster_labels)
print(cm)
# Calculate purity/accuracy (handling potential label swap)
# If the clustering is inverted, 1-accuracy is the true accuracy
acc = accuracy_score(y, cluster_labels)
print(f"\nClustering Accuracy (Approx): {max(acc, 1-acc)*100:.2f}%")
R E S U L T S:
Visualization
--- Confusion Matrix (Clusters vs Actual) ---
[[ 36 176]
 [339  18]]
Clustering Accuracy (Approx): 90.51%
 Computer Science and Engineering
32 of 33

BCS606 Machine Learning Lab 33
   Computer Science and Engineering 33 of 33
