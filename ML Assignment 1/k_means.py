import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn_extra.cluster import KMedoids
from sklearn.metrics import pairwise_distances_argmin_min
from scipy.stats import entropy

# Load the dataset
data = pd.read_csv("iris.csv")

# Display the first few rows of the dataset to understand its structure
print(data.head())


# Extracting features (attributes) for clustering
X = data.iloc[:, :-1].values

# K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
kmeans_labels = kmeans.labels_
kmeans_centers = kmeans.cluster_centers_

# Plotting the clusters
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap='viridis')
plt.scatter(kmeans_centers[:, 0], kmeans_centers[:, 1], c='red', marker='x', s=200, label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('PetalLenghtCm')
plt.ylabel('PetalWidhtCm')
plt.legend()
plt.show()

# Counting number of points in each cluster
kmeans_counts = np.bincount(kmeans_labels)
print("Number of points in each cluster (K-Means):", kmeans_counts)

# Calculating Sum of Squared Errors (SSE)
kmeans_sse = np.sum((X - kmeans_centers[kmeans_labels]) ** 2)
print("Sum of Squared Errors (SSE) for K-Means:", kmeans_sse)



# Creating dimensionality-reduced data for plotting
X_reduced = X[:, 0] * 7 + X[:, 2] * 3, X[:, 1] * 11 + X[:, 3]

# Plotting dimensionality-reduced data
plt.figure(figsize=(10, 6))

# Plotting K-Means clusters on reduced dimensions
plt.subplot(1, 2, 1)
plt.scatter(X_reduced[0], X_reduced[1], c=kmeans_labels, cmap='viridis')
plt.scatter(kmeans_centers[:, 0] * 7 + kmeans_centers[:, 2] * 3, kmeans_centers[:, 1] * 11 + kmeans_centers[:, 3], c='red', marker='x', s=200, label='Centroids (K-Means)')
plt.title('K-Means Clustering (Reduced Dimensions)')
plt.xlabel('Reduced Feature 1')
plt.ylabel('Reduced Feature 2')
plt.legend()


plt.tight_layout()
plt.show()






# Ground truth labels for the Iris dataset
true_labels = data['Species'].map({'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2})

# Calculate Shannon's Entropy for K-Means
kmeans_entropy = entropy(np.bincount(kmeans_labels), base=2)
print("\nShannon's Entropy for K-Means:", kmeans_entropy)


