import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score



# Data Loading and Preprocessing. Load the data and set the first row as the header and select the relevant attributes (maximum 10)
# data = pd.read_csv(path, header=0)
student_db = pd.read_csv("students.csv", header=0)
student_db = student_db.drop_duplicates()

# Select relevant attributes (max 10)
relevant_attributes = ['gradyear', 'age', 'NumberOffriends', 'basketball','football', 'soccer', 'softball', 'volleyball', 'swimming', 'cheerleading']
data = student_db[relevant_attributes]


# Replace non-numeric values with NaN
data = data.apply(lambda x: pd.to_numeric(x, errors='coerce'))
# Handle missing values
data = data.dropna(subset=relevant_attributes)
# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)



# DBSCAN Clustering
db = DBSCAN(eps=0.5, min_samples=5).fit(scaled_data)
labels = db.labels_
# Plot DBSCAN clusters
plt.figure(figsize=(10, 6))
unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black for noise
        col = 'k'
    class_members = [index for index, label in enumerate(labels) if label == k]
    cluster_data = scaled_data[class_members]
    plt.scatter(cluster_data[:, 0], cluster_data[:, 1], s=50, c=col, marker='o', label='Cluster {}'.format(k))

plt.title('DBSCAN Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()


# Count points in each DBSCAN cluster
cluster_counts = pd.Series(labels).value_counts()
print('DBSCAN Cluster Counts:\n', cluster_counts)

# Silhouette Score for DBSCAN
silhouette_avg = silhouette_score(scaled_data, labels)
print(f'Silhouette Score for DBSCAN: {silhouette_avg:.3f}')


# Hierarchical Clustering
hier_clust = AgglomerativeClustering(n_clusters=3).fit(scaled_data)
hier_labels = hier_clust.labels_
# Plot Hierarchical clusters
plt.figure(figsize=(10, 6))
unique_labels = set(hier_labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    class_members = [index for index, label in enumerate(hier_labels) if label== k]
    cluster_data = scaled_data[class_members]
    plt.scatter(cluster_data[:, 0], cluster_data[:, 1], s=50, c=col, marker='o', label='Cluster {}'.format(k))

plt.title('Hierarchical Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()


# Count points in each Hierarchical cluster
cluster_counts = pd.Series(hier_labels).value_counts()
print('\nHierarchical Cluster Counts:\n', cluster_counts)

# Silhouette Score for Hierarchical Clustering
silhouette_avg = silhouette_score(scaled_data, hier_labels)
print(f'Silhouette Score for Hierarchical Clustering: {silhouette_avg:.3f}')