import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.metrics import pairwise_distances
from sklearn import metrics

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data  # Features
y = iris.target  # Target

# Convert to DataFrame for convenience
iris_df = pd.DataFrame(X, columns=iris.feature_names)

# Display the first few rows of the dataset to understand its structure
print(iris_df.head())


# Elbow method
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plotting the elbow method graph
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')  # Within cluster sum of squares
plt.show()


def dunn_index(X, labels):
    cluster_distances = []
    for label in np.unique(labels):
        cluster_points = X[labels == label]
        if len(cluster_points) > 1:
            pairwise_distances_cluster = pairwise_distances(cluster_points)
            cluster_distances.append(np.max(pairwise_distances_cluster))
    
    if cluster_distances:
        max_intra_cluster_distance = max(cluster_distances)
    else:
        max_intra_cluster_distance = 0
        
    min_inter_cluster_distance = np.inf
    for i in range(len(cluster_distances)):
        for j in range(i + 1, len(cluster_distances)):
            inter_cluster_distance = pairwise_distances(cluster_points[i].reshape(-1, 1), cluster_points[j].reshape(-1, 1)).min()
            if inter_cluster_distance < min_inter_cluster_distance:
                min_inter_cluster_distance = inter_cluster_distance
                
    dunn_index = min_inter_cluster_distance / max_intra_cluster_distance
    return dunn_index


# Find optimal k using elbow method
optimal_k = 3  # Choose the number of clusters based on the elbow method

# Apply k-means clustering with the optimal k
kmeans = KMeans(n_clusters=optimal_k)
kmeans.fit(X)

# Calculate Dunn index
dunn_index_value = dunn_index(X, kmeans.labels_)
print("Dunn index:", dunn_index_value)


# Calculate Davies Bouldin index
davies_bouldin_index = davies_bouldin_score(X, kmeans.labels_)
print("Davies Bouldin index:", davies_bouldin_index)


# Calculate Silhouette index
silhouette_avg = silhouette_score(X, kmeans.labels_)
print("Silhouette index:", silhouette_avg)


# Plotting cluster distributions for each feature (2D form)
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

for i in range(len(iris.feature_names)):
    row = i // 3
    col = i % 3
    axs[row, col].scatter(X[:, i], X[:, (i+1) % 4], c=kmeans.labels_, cmap='viridis')
    axs[row, col].set_title(iris.feature_names[i] + ' vs ' + iris.feature_names[(i+1) % 4])
    axs[row, col].set_xlabel(iris.feature_names[i])
    axs[row, col].set_ylabel(iris.feature_names[(i+1) % 4])

plt.tight_layout()
plt.show()
