import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

class CureCluster:
    def __init__(self, points):
        self.points = points
        self.center = np.mean(points, axis=0)

    @staticmethod
    def hierarchical_clustering(points, k):
        clusters = [CureCluster([point]) for point in points]

        while len(clusters) > k:
            min_distance = float("inf")
            merge_index = (0, 0)

            for i in range(len(clusters) - 1):
                for j in range(i + 1, len(clusters)):
                    distance = np.linalg.norm(clusters[i].center - clusters[j].center)
                    if distance < min_distance:
                        min_distance = distance
                        merge_index = (i, j)

            merged_cluster = CureCluster(
                clusters[merge_index[0]].points + clusters[merge_index[1]].points
            )
            clusters.pop(merge_index[1])
            clusters[merge_index[0]] = merged_cluster

        return clusters

    @staticmethod
    def plot_clusters(clusters):
        plt.figure(figsize=(10, 6))

        for i, cluster in enumerate(clusters):
            cluster_points = np.array(cluster.points)

            plt.scatter(
                cluster_points[:, 0], cluster_points[:, 1], label=f"Cluster{i + 1}"
            )

        plt.title("CURE Clustering")
        plt.xlabel("Sepal Length (cm)")
        plt.ylabel("Sepal Width (cm)")
        plt.legend()
        plt.show()

# Loading Iris dataset
iris = load_iris()
data = iris.data[:, :2]

# Perform hierarchical clustering with CURE
k = 3
clusters = CureCluster.hierarchical_clustering(data, k)

# Plot the resulting clusters
CureCluster.plot_clusters(clusters)
