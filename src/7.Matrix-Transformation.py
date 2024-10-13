"""
Matrix Transformation (medium)

Write a Python function that transforms a given matrix A using the operation T^{-1}AS, where T and S are invertible
matrices. The function should first validate if the matrices T and S are invertible, and then perform the 
transformation. In cases where there is no solution return -1.

Example:
        input: A = [[1, 2], [3, 4]], T = [[2, 0], [0, 2]], S = [[1, 1], [0, 1]]
        output: [[0.5,1.5],[1.5,3.5]]
        reasoning: The matrices T and S are used to transform matrix A by computing T^{-1}AS.
"""

import numpy as np


def transform_matrix(A, T, S):
    A = np.asarray(A)
    T = np.asarray(T)
    S = np.asarray(S)
    if not np.linalg.det(T) or not np.linalg.det(S):
        return -1
    transformed_matrix = np.dot(np.dot(np.linalg.inv(T), A), S)
    transformed_matrix = transformed_matrix.tolist()
    return transformed_matrix


if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    T = [[2, 0], [0, 2]]
    S = [[1, 1], [0, 1]]
    print(transform_matrix(A, T, S))
