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

# K-Medoids clustering
kmedoids = KMedoids(n_clusters=3, random_state=42)
kmedoids.fit(X)
kmedoids_labels = kmedoids.labels_
kmedoids_centers = X[kmedoids.medoid_indices_]

# Plotting the clusters
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=kmedoids_labels, cmap='viridis')
plt.scatter(kmedoids_centers[:, 0], kmedoids_centers[:, 1], c='red', marker='x', s=200, label='Medoids')
plt.title('K-Medoids Clustering')
plt.xlabel('PetalLenghtCm')
plt.ylabel('PetalWidhtCm')
plt.legend()
plt.show()

# Counting number of points in each cluster
kmedoids_counts = np.bincount(kmedoids_labels)
print("Number of points in each cluster (K-Medoids):", kmedoids_counts)

# Calculating Sum of Squared Errors (SSE)
kmedoids_sse = np.sum(pairwise_distances_argmin_min(X, kmedoids_centers)[1] ** 2)
print("Sum of Squared Errors (SSE) for K-Medoids:", kmedoids_sse)


# Creating dimensionality-reduced data for plotting
X_reduced = X[:, 0] * 7 + X[:, 2] * 3, X[:, 1] * 11 + X[:, 3]

# Plotting dimensionality-reduced data
plt.figure(figsize=(10, 6))

# Plotting K-Medoids clusters on reduced dimensions
plt.subplot(1, 2, 2)
plt.scatter(X_reduced[0], X_reduced[1], c=kmedoids_labels, cmap='viridis')
plt.scatter(kmedoids_centers[:, 0] * 7 + kmedoids_centers[:, 2] * 3, kmedoids_centers[:, 1] * 11 + kmedoids_centers[:, 3], c='red', marker='x', s=200, label='Medoids (K-Medoids)')
plt.title('K-Medoids Clustering (Reduced Dimensions)')
plt.xlabel('PetalLenghtCm')
plt.ylabel('PetalWidhtCm')
plt.legend()

plt.tight_layout()
plt.show()


# Ground truth labels for the Iris dataset
true_labels = data['Species'].map({'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2})

# Calculating Shannon's Entropy for K-Medoids
kmedoids_entropy = entropy(np.bincount(kmedoids_labels), base=2)
print("Shannon's Entropy for K-Medoids:", kmedoids_entropy)


