from sklearn.cluster import KMeans
import numpy as np

import pandas

df = pandas.read_csv("C:/Users/diepw/Downloads/Ag Ed for All - Groupings - asd.csv", 
                         usecols = ['Name', 'Lat & Long'])

print(df)
quit()
# Define the latitude and longitude points
points = np.array([
    [40.412483, -91.392114],
    [40.577006, -91.518805],
    # ... (add the remaining points here)
])

# Perform k-means clustering with 24 clusters
kmeans = KMeans(n_clusters=24, random_state=0).fit(points)

# Retrieve the cluster labels
cluster_labels = kmeans.labels_

# Print the cluster labels for each point
for i, label in enumerate(cluster_labels):
    print(f"Point {i+1}: Cluster {label+1}")