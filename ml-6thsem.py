ML Lab Easy Programs (1–5) + Open-Ended (Short Versions)
Program 1 – Histograms & Boxplots
       import pandas as pd
       import matplotlib.pyplot as plt
       from sklearn.datasets import fetch_california_housing
       data = fetch_california_housing(as_frame=True)
       df = data.frame
        df.hist(figsize=(10,8))
        plt.show()
       df.plot(kind='box', subplots=True, layout=(3,3), figsize=(10,8))
       plt.show()
Program 2 – Correlation & Heatmap
       import seaborn as sns
       import matplotlib.pyplot as plt
       from sklearn.datasets import fetch_california_housing
       data = fetch_california_housing(as_frame=True)
       df = data.frame
       sns.heatmap(df.corr(), annot=True)
       plt.show()
Program 3 – PCA
       from sklearn.datasets import load_iris
       from sklearn.decomposition import PCA
       import matplotlib.pyplot as plt
        iris = load_iris()
        X = iris.data
        y = iris.target
       pca = PCA(n_components=2)
       X_pca = pca.fit_transform(X)
       plt.scatter(X_pca[:,0], X_pca[:,1], c=y)
       plt.show()
Program 4 – Find-S Algorithm
       import pandas as pd
       data = pd.read_csv("data.csv")
        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]
h = None
       for i in range(len(data)):
           if y[i] == "Yes":
               if h is None:
                   h = list(X.iloc[i])
               else:
                   for j in range(len(h)):
                       if h[j] != X.iloc[i][j]:
                           h[j] = '?'
print("Final Hypothesis:", h)

Program 5 – KNN
import numpy as np
from collections import Counter
data = np.random.rand(100)
train = data[:50]
test = data[50:]
labels = ["Class1" if x <= 0.5 else "Class2" for x in train]
def knn(train, labels, point, k):
    dist = sorted([(abs(point - train[i]), labels[i]) for i in range(len(train))])
    return Counter([l for _, l in dist[:k]]).most_common(1)[0][0]
for k in [1,3,5]:
    print("k =", k)
    for x in test[:5]:
        print(knn(train, labels, x, k))

Open-Ended 1 – Feature Selection (Simple)
       from sklearn.datasets import load_iris
       from sklearn.linear_model import LogisticRegression
       from sklearn.model_selection import train_test_split
       data = load_iris(as_frame=True).frame
       X = data.drop("target", axis=1)
       y = data["target"]
       X_train,X_test,y_train,y_test = train_test_split(X,y)
       model = LogisticRegression(max_iter=200)
       model.fit(X_train,y_train)
       print("Accuracy:", model.score(X_test,y_test))
Open-Ended 2 – KNN Distance
       from sklearn.datasets import load_iris
       from sklearn.neighbors import KNeighborsClassifier
       X,y = load_iris(return_X_y=True)
       for m in ["euclidean","manhattan"]:
           model = KNeighborsClassifier(metric=m)
           model.fit(X,y)
           print(m, "done")
Open-Ended 3 – PCA Impact
       from sklearn.datasets import load_iris
       from sklearn.decomposition import PCA
       X,y = load_iris(return_X_y=True)
       for n in [2,3]:
           pca = PCA(n_components=n)
           X_new = pca.fit_transform(X)
           print("Reduced to", n)
Open-Ended 4 – Feature Scaling
       from sklearn.datasets import load_iris
       from sklearn.preprocessing import StandardScaler
       X,y = load_iris(return_X_y=True)
       scaler = StandardScaler()
       X_scaled = scaler.fit_transform(X)
        print("Scaling done")
