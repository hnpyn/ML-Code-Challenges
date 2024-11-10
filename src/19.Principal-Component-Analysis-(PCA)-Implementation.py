"""
Principal Component Analysis (PCA) Implementation (medium)
Write a Python function that performs Principal Component Analysis (PCA) from scratch. The function should take a 2D 
NumPy array as input, where each row represents a data sample and each column represents a feature. The function should 
standardize the dataset, compute the covariance matrix, find the eigenvalues and eigenvectors, and return the principal 
components (the eigenvectors corresponding to the largest eigenvalues). The function should also take an integer k as 
input, representing the number of principal components to return.

Example:
        input: data = np.array([[1, 2], [3, 4], [5, 6]]), k = 1
        output:  [[0.7071], [0.7071]]
        reasoning: After standardizing the data and computing the covariance matrix, the eigenvalues and eigenvectors 
        are calculated. The largest eigenvalue's corresponding eigenvector is returned as the principal component, 
        rounded to four decimal places.
"""

import numpy as np


def pca(data, k):
    norm_data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)
    cov_matrix = np.cov(norm_data, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    idx = np.argsort(eigenvalues)[::-1]
    principal_components = np.round(eigenvectors[:, idx[:k]], 4).tolist()
    return principal_components


if __name__ == "__main__":
    data = np.array([[1, 2], [3, 4], [5, 6]])
    k = 1
    print(pca(data, k))
