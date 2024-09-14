import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from yellowbrick.cluster import KElbowVisualizer, SilhouetteVisualizer
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import pdist, squareform

# Suppress the warning
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Load the dataset
iris = pd.read_csv("Iris.csv")
# Set the first row as header
iris.columns = iris.iloc[0]
iris = iris.iloc[1:]
# Extract the features
X = iris.iloc[:, 1:5].values


# Elbow method to find optimal number of clusters
visualizer = KElbowVisualizer(KMeans(), k=(2, 12))
visualizer.fit(X)
visualizer.show()



# Dunn index for cluster validity
def dunn(X, labels):
    distances = pairwise_distances(X)
    # Initialize minimum inter-cluster distance
    min_inter_cluster_distance = np.inf
    # Initialize maximum intra-cluster diameter
    max_intra_cluster_diameter = -np.inf
    # Iterate over each cluster
    for cluster_label in np.unique(labels):
        cluster_points = X[labels == cluster_label]
        # Calculate intra-cluster diameter
        intra_cluster_diameter = np.max(pdist(cluster_points))
        if intra_cluster_diameter > max_intra_cluster_diameter:
            max_intra_cluster_diameter = intra_cluster_diameter

        # Calculate inter-cluster distances
        other_cluster_points = X[labels != cluster_label]
        inter_cluster_distances = pairwise_distances(cluster_points, other_cluster_points).min(axis=1)

        # Update minimum inter-cluster distance
        if inter_cluster_distances.min() < min_inter_cluster_distance:
            min_inter_cluster_distance = inter_cluster_distances.min()
    # Dunn index = minimum inter-cluster distance / maximum intra-cluster diameter
    return min_inter_cluster_distance / max_intra_cluster_diameter

dunn_scores = []
for n_clusters in range(2, 11):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)
    dunn_scores.append(dunn(X, labels))

dunn_optimal_cluster = np.argmax(dunn_scores) + 2
print(f'Optimal number of clusters based on Dunn index: {dunn_optimal_cluster}')


# Davies-Bouldin index for cluster validity
davies_bouldin_scores = []
for n_clusters in range(2, 11):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)
    davies_bouldin_scores.append(davies_bouldin_score(X, labels))

davies_bouldin_optimal_cluster = np.argmin(davies_bouldin_scores) + 2
print(f'Optimal number of clusters based on Davies-Bouldin index: {davies_bouldin_optimal_cluster}')



# Silhouette index for cluster similarity
silhouette_scores = []
for n_clusters in range(2, 11):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)
    silhouette_scores.append(silhouette_score(X, labels))

silhouette_optimal_cluster = np.argmax(silhouette_scores) + 2
print(f'Optimal number of clusters based on Silhouette index:{silhouette_optimal_cluster}')

# Visualize the silhouette scores for different cluster counts
visualizer = SilhouetteVisualizer(KMeans(), colors='yellowbrick')
visualizer.fit(X)
visualizer.show()


# Plot cluster distributions for each feature
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)
# Create a scatter plot for each pair of features
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
axs = axs.ravel()
for i, (x, y) in enumerate([(0, 1), (0, 2), (0, 3), (1, 2)]):
    axs[i].scatter(X[:, x], X[:, y], c=labels, cmap='viridis')
    axs[i].set_xlabel(iris.columns[x + 1])
    axs[i].set_ylabel(iris.columns[y + 1])
    axs[i].set_title(f'Feature {iris.columns[x + 1]} vs {iris.columns[y + 1]}')
plt.tight_layout()
plt.show()