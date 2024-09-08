# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram

# Read the CSV file into a DataFrame
df = pd.read_csv("students.csv")

# Select relevant attributes
attributes = ['gradyear', 'age', 'NumberOffriends', 'basketball', 'football', 'soccer', 'softball', 'volleyball', 'swimming', 'cheerleading']

# Preprocess the data
X = df[attributes].fillna(0)  # Fill missing values with 0, assuming they represent absence

# Convert non-numeric values to NaN
X = X.apply(pd.to_numeric, errors='coerce')

# Fill NaN values with 0
X = X.fillna(0)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# DBSCAN clustering
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan.fit(X_scaled)
labels = dbscan.labels_


# Plotting DBSCAN clusters
plt.figure(figsize=(10, 6))
plt.subplot(1, 1, 1)
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=dbscan.labels_, cmap='viridis')
plt.title('DBSCAN Clusters')
plt.xlabel('gradyear')
plt.ylabel('age')

# Count points in each DBSCAN cluster
cluster_counts = pd.Series(labels).value_counts()
print('DBSCAN Cluster Counts:\n', cluster_counts)

# Calculating the Silhouette Score for DBSCAN
silhouette_avg = silhouette_score(X_scaled, dbscan.labels_)
print("DBSCAN Silhouette Score:", silhouette_avg)

plt.show()


# Hierarchical clustering

hierarchical = AgglomerativeClustering(n_clusters=None, distance_threshold=0.5)  # Adjust distance threshold as needed
hierarchical_labels = hierarchical.fit_predict(X_scaled)


# Plotting Hierarchical clusters
plt.figure(figsize=(10, 6))
plt.subplot(1, 1, 1)
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=hierarchical.labels_, cmap='viridis')
plt.title('Hierarchical Clusters')
plt.xlabel('gradyear')
plt.ylabel('age')


# Count points in each Hierarchical cluster
cluster_counts = pd.Series(hierarchical_labels).value_counts()
print('\nHierarchical Cluster Counts:\n', cluster_counts)

# Calculate the Silhouette Score for Hierarchical Clustering
silhouette_avg_hierarchical = silhouette_score(X_scaled, hierarchical_labels)
print("Hierarchical Clustering Silhouette Score:", silhouette_avg_hierarchical)

plt.show()