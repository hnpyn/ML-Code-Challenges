"""
K-Means Clustering (medium)

Your task is to write a Python function that implements the k-Means clustering algorithm. This function should take 
specific inputs and produce a list of final centroids. k-Means clustering is a method used to partition n points into 
k clusters. The goal is to group similar points together and represent each group by its center (called the centroid).

Function Inputs:
    points: A list of points, where each point is a tuple of coordinates (e.g., (x, y) for 2D points)
    k: An integer representing the number of clusters to form
    initial_centroids: A list of initial centroid points, each a tuple of coordinates
    max_iterations: An integer representing the maximum number of iterations to perform
Function Output:
    A list of the final centroids of the clusters, where each centroid is rounded to the nearest fourth decimal.

Example:
        input: points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)], k = 2,
        initial_centroids = [(1, 1), (10, 1)], max_iterations = 10
        output: [(1, 2), (10, 2)]
        reasoning: Given the initial centroids and a maximum of 10 iterations,the points are clustered around these 
        points, and the centroids are updated to the mean of the assigned points, resulting in the final centroids 
        which approximate the means of the two clusters. The exact number of iterations needed may vary, but the 
        process will stop after 10 iterations at most.
"""


def k_means_clustering(points, k, initial_centroids, max_iterations):
    def calculate_distance(point, centroid):
        return sum([(point[i] - centroid[i]) ** 2 for i in range(len(point))])

    final_centroids = initial_centroids
    for i in range(max_iterations):
        clusters = [[] for _ in range(k)]
        tmp_centroids = [[] for _ in range(k)]
        for point in points:
            distances = [calculate_distance(point, centroid) for centroid in final_centroids]
            closest_cluster = distances.index(min(distances))
            clusters[closest_cluster].append(point)
        for i in range(k):
            if clusters[i]:
                tmp_centroids[i] = tuple(round(sum(coord) / len(clusters[i]), 4) for coord in zip(*clusters[i]))
            else:
                tmp_centroids[i] = final_centroids[i]
        if tmp_centroids == final_centroids:
            break
        else:
            final_centroids = tmp_centroids

    return final_centroids


if __name__ == "__main__":
    points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)]
    k = 2
    initial_centroids = [(1, 1), (10, 1)]
    max_iterations = 10
    print(k_means_clustering(points, k, initial_centroids, max_iterations))
