# -*- coding: utf-8 -*-
"""Iris Clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x48l9P1GEnrhOT02xgdIhx8AohmeWhLQ

Importing Dependencies
"""

import pandas as pd
import numpy as np

# Importing dataset
df = pd.read_csv('/content/drive/MyDrive/PROJECTS/Iris Classification/iris dataset/Iris.csv')

df.head()

df.shape

"""We're going to predict using unsupervised learning so  we don't need the Species column. Let's remove it

"""

iris_clustering = df.drop(columns=['Species'])

iris_clustering.head()

"""Now, Features needs to be selected on which basis clusterung will be done.
Possible combos:
1. SepalLength vs Sepal width
2. sepal length vs petal length
3. sepal length vs petal width
4. sepal width vs petal length
5. sepal width vs petal width
7. petal lentgh vs petal width

# 1. SepalLength vs Sepal width
"""

X = iris_clustering.iloc[:, [0, 1]].values # Taking values from column 0 and 1 from iris_clustering dataset

"""Choosing Number of Clusters

WCSS
"""

# Elbow method to determine the optimum number of values
from sklearn.cluster import KMeans
wcss=[]
for i in range(1, 11): # Checking 1 to 10 clusters of data
  Kmeans = KMeans(n_clusters=i, init='k-means++', random_state=24)
  Kmeans.fit(X)
  #  Appending the wcss values to the list
  wcss.append(Kmeans.inertia_) # Kmeans.inertia_ returns the wcss value for an initialized cluster

"""

Plotting the elbow graph
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Elbow Graph
sns.set()
plt.plot(range(1, 11), wcss)
plt.title("Elbow Point Graph")
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

"""We can see WCSS value drops for 1, 2, 3 cluters but after 3 Wcss value decreases gradually.
As after 3 there is no significant amount of drop in wcss value , The optimum number of cluster is 3.
"""

# initializing the K-Means with optimum number of clusters
Kmeans = KMeans(n_clusters=3, init='k-means++', random_state=0)

# Fitting the datapoints to the kmeans function and returning label for each data points
y = Kmeans.fit_predict(X)

print(y)

"""Visualizing the clusters"""

plt.scatter(X[y==0, 0], X[y==0, 1], s = 50, c = "red", label = "Cluster-1")
plt.scatter(X[y==1, 0], X[y==1, 1], s = 50, c = "blue", label = "Cluster-2")
plt.scatter(X[y==2, 0], X[y==2, 1], s = 50, c = "green", label = "Cluster-3")
plt.scatter(Kmeans.cluster_centers_[:, 0], Kmeans.cluster_centers_[:, 1], s=100, c='cyan', label = "CENTROIDS")
plt.title("Iris Flower Clustering")
plt.xlabel('Sepal Width')
plt.ylabel("Petal Width")
plt.legend()
plt.show()



"""# 2. Sepal length vs Petal Length"""

X = iris_clustering.iloc[:, [0, 2]].values # Taking values from column 0 and 1 from iris_clustering dataset
# Elbow method to determine the optimum number of values
from sklearn.cluster import KMeans
wcss=[]
for i in range(1, 11): # Checking 1 to 10 clusters of data
  Kmeans = KMeans(n_clusters=i, init='k-means++', random_state=24)
  Kmeans.fit(X)
  #  Appending the wcss values to the list
  wcss.append(Kmeans.inertia_) # Kmeans.inertia_ returns the wcss value for an initialized cluster

# Elbow Graph
sns.set()
plt.plot(range(1, 11), wcss)
plt.title("Elbow Point Graph")
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# initializing the K-Means with optimum number of clusters
Kmeans = KMeans(n_clusters=3, init='k-means++', random_state=0)

# Fitting the datapoints to the kmeans function and returning label for each data points
y = Kmeans.fit_predict(X)

plt.scatter(X[y==0, 0], X[y==0, 1], s = 50, c = "red", label = "Cluster-1")
plt.scatter(X[y==1, 0], X[y==1, 1], s = 50, c = "blue", label = "Cluster-2")
plt.scatter(X[y==2, 0], X[y==2, 1], s = 50, c = "green", label = "Cluster-3")
plt.scatter(Kmeans.cluster_centers_[:, 0], Kmeans.cluster_centers_[:, 1], s=100, c='cyan', label = "CENTROIDS")
plt.title("Iris Flower Clustering")
plt.xlabel('Sepal Width')
plt.ylabel("Petal Width")
plt.legend()
plt.show()

"""# 3. Sepal Length vs Petal Width"""

X = iris_clustering.iloc[:, [0, 3]].values # Taking values from column 0 and 1 from iris_clustering dataset
# Elbow method to determine the optimum number of values
from sklearn.cluster import KMeans
wcss=[]
for i in range(1, 11): # Checking 1 to 10 clusters of data
  Kmeans = KMeans(n_clusters=i, init='k-means++', random_state=24)
  Kmeans.fit(X)
  #  Appending the wcss values to the list
  wcss.append(Kmeans.inertia_) # Kmeans.inertia_ returns the wcss value for an initialized cluster

# Elbow Graph
sns.set()
plt.plot(range(1, 11), wcss)
plt.title("Elbow Point Graph")
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# initializing the K-Means with optimum number of clusters
Kmeans = KMeans(n_clusters=3, init='k-means++', random_state=0)

# Fitting the datapoints to the kmeans function and returning label for each data points
y = Kmeans.fit_predict(X)

plt.scatter(X[y==0, 0], X[y==0, 1], s = 50, c = "red", label = "Cluster-1")
plt.scatter(X[y==1, 0], X[y==1, 1], s = 50, c = "blue", label = "Cluster-2")
plt.scatter(X[y==2, 0], X[y==2, 1], s = 50, c = "green", label = "Cluster-3")
plt.scatter(Kmeans.cluster_centers_[:, 0], Kmeans.cluster_centers_[:, 1], s=100, c='cyan', label = "CENTROIDS")
plt.title("Iris Flower Clustering")
plt.xlabel('Sepal Width')
plt.ylabel("Petal Width")
plt.legend()
plt.show()



"""# 4. Sepal width vs Petal Length"""

X = iris_clustering.iloc[:, [1, 3]].values # Taking values from column 0 and 1 from iris_clustering dataset
# Elbow method to determine the optimum number of values
from sklearn.cluster import KMeans
wcss=[]
for i in range(1, 11): # Checking 1 to 10 clusters of data
  Kmeans = KMeans(n_clusters=i, init='k-means++', random_state=24)
  Kmeans.fit(X)
  #  Appending the wcss values to the list
  wcss.append(Kmeans.inertia_) # Kmeans.inertia_ returns the wcss value for an initialized cluster

# Elbow Graph
sns.set()
plt.plot(range(1, 11), wcss)
plt.title("Elbow Point Graph")
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# initializing the K-Means with optimum number of clusters
Kmeans = KMeans(n_clusters=3, init='k-means++', random_state=0)

# Fitting the datapoints to the kmeans function and returning label for each data points
y = Kmeans.fit_predict(X)

plt.scatter(X[y==0, 0], X[y==0, 1], s = 50, c = "red", label = "Cluster-1")
plt.scatter(X[y==1, 0], X[y==1, 1], s = 50, c = "blue", label = "Cluster-2")
plt.scatter(X[y==2, 0], X[y==2, 1], s = 50, c = "green", label = "Cluster-3")
plt.scatter(Kmeans.cluster_centers_[:, 0], Kmeans.cluster_centers_[:, 1], s=100, c='cyan', label = "CENTROIDS")
plt.title("Iris Flower Clustering")
plt.xlabel('Sepal Width')
plt.ylabel("Petal Width")
plt.legend()
plt.show()

"""# 5. Sepal Width vs Petal Width"""

X = iris_clustering.iloc[:, [1, 3]].values # Taking values from column 1 and 3 from iris_clustering dataset

print(X)

"""Choosing number of clusters

WCSS - Withis Clusters Sum of Squares
"""

# Elbow method to determine the optimum number of values
from sklearn.cluster import KMeans

wcss=[]
for i in range(1, 11): # Checking 1 to 10 clusters of data
  Kmeans = KMeans(n_clusters=i, init='k-means++', random_state=24)
  Kmeans.fit(X)
  #  Appending the wcss values to the list
  wcss.append(Kmeans.inertia_) # Kmeans.inertia_ returns the wcss value for an initialized cluster

"""Plotting the Elbow Graph"""

import matplotlib.pyplot as plt
import seaborn as sns

# Elbow Graph
sns.set()
plt.plot(range(1, 11), wcss)
plt.title("Elbow Point Graph")
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

"""We can see WCSS value drops for 1, 2, 3 cluters but after 3 Wcss value decreases gradually.
As after 3 there is no significant amount of drop in wcss value , The optimum number of cluster is 3.
"""

# initializing the K-Means with optimum number of clusters
Kmeans = KMeans(n_clusters=3, init='k-means++', random_state=0)

# Fitting the datapoints to the kmeans function and returning label for each data points
y = Kmeans.fit_predict(X)

print(y)

"""Visualizing the Clusters"""

# Scatter plot for (x, y) with label 0 as cluster 1 in color red
plt.scatter(X[y==0, 0], X[y==0, 1], s = 50, c = "red", label = "Cluster-1")

# Scatter plot for (x, y) with label 1 as cluster 2 in color red
plt.scatter(X[y==1, 0], X[y==1, 1], s = 50, c = "blue", label = "Cluster-2")

# Scatter plot for (x, y) with label 2 as cluster 3 in color green
plt.scatter(X[y==2, 0], X[y==2, 1], s = 50, c = "green", label = "Cluster-3")

# Plotting the centroid of clusters
plt.scatter(Kmeans.cluster_centers_[:, 0], Kmeans.cluster_centers_[:, 1], s=100, c='cyan', label = "CENTROIDS")
plt.title("Iris Flower Clustering")
plt.xlabel('Sepal Width')
plt.ylabel("Petal Width")
plt.show()

plt.scatter(X[y==0, 0], X[y==0, 1], s = 50, c = "red", label = "Cluster-1")
plt.scatter(X[y==1, 0], X[y==1, 1], s = 50, c = "blue", label = "Cluster-2")
plt.scatter(X[y==2, 0], X[y==2, 1], s = 50, c = "green", label = "Cluster-3")
plt.scatter(Kmeans.cluster_centers_[:, 0], Kmeans.cluster_centers_[:, 1], s=100, c='cyan', label = "CENTROIDS")
plt.title("Iris Flower Clustering")
plt.xlabel('Sepal Width')
plt.ylabel("Petal Width")
plt.legend()
plt.show()



"""# 6. Petal Length vs Petal Width"""

X = iris_clustering.iloc[:, [2, 3]].values # Taking values from column 0 and 1 from iris_clustering dataset
# Elbow method to determine the optimum number of values
from sklearn.cluster import KMeans
wcss=[]
for i in range(1, 11): # Checking 1 to 10 clusters of data
  Kmeans = KMeans(n_clusters=i, init='k-means++', random_state=24)
  Kmeans.fit(X)
  #  Appending the wcss values to the list
  wcss.append(Kmeans.inertia_) # Kmeans.inertia_ returns the wcss value for an initialized cluster

# Elbow Graph
sns.set()
plt.plot(range(1, 11), wcss)
plt.title("Elbow Point Graph")
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# initializing the K-Means with optimum number of clusters
Kmeans = KMeans(n_clusters=3, init='k-means++', random_state=0)

# Fitting the datapoints to the kmeans function and returning label for each data points
y = Kmeans.fit_predict(X)

plt.scatter(X[y==0, 0], X[y==0, 1], s = 50, c = "red", label = "Cluster-1")
plt.scatter(X[y==1, 0], X[y==1, 1], s = 50, c = "blue", label = "Cluster-2")
plt.scatter(X[y==2, 0], X[y==2, 1], s = 50, c = "green", label = "Cluster-3")
plt.scatter(Kmeans.cluster_centers_[:, 0], Kmeans.cluster_centers_[:, 1], s=100, c='cyan', label = "CENTROIDS")
plt.title("Iris Flower Clustering")
plt.xlabel('Sepal Width')
plt.ylabel("Petal Width")
plt.legend()
plt.show()

"""# # Conclusion :

![iris bes.png](data:image/png;base64,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)

This is the clustering of Sepal Length vs Petal Width Clustering. We can clearly see that three clusters are distuinguished far better than any other combinations clusters.
"""