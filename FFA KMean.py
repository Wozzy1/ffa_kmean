from sklearn.cluster import KMeans
import numpy as np
import pandas

df = pandas.read_csv("C:/Users/diepw/Downloads/Ag Ed for All - Groupings - asd.csv", 
                         usecols = ['Name', 'Lat & Long'])

#print(df)

coords_ = df['Lat & Long'].tolist()
coords = [(float(lat), float(lon)) for lat, lon in coords_]

quit()
kmeans = KMeans(n_clusters=24, random_state=0).fit(coords_)

cluster_labels = kmeans.labels_

for i, label in enumerate(cluster_labels):
    print(f"Point {i+1}: Cluster {label+1}")

"""
# Define the latitude and longitude points
points = np.array()

# Perform k-means clustering with 24 clusters
kmeans = KMeans(n_clusters=24, random_state=0).fit(points)

# Retrieve the cluster labels
cluster_labels = kmeans.labels_

# Print the cluster labels for each point
for i, label in enumerate(cluster_labels):
    print(f"Point {i+1}: Cluster {label+1}")"""