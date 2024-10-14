"""
Singular Value Decomposition (SVD) (hard)

Write a Python function that approximates the Singular Value Decomposition on a 2x2 matrix by using the jacobian method 
and without using numpy svd function, i mean you could but you wouldn't learn anything. return the result in this 
format.

Example:
        input: a = [[2, 1], [1, 2]]
        output: (array([[-0.70710678, -0.70710678],
                        [-0.70710678,  0.70710678]]),
        array([3., 1.]),
        array([[-0.70710678, -0.70710678],
               [-0.70710678,  0.70710678]]))
        reasoning: U is the first matrix sigma is the second vector and V is the third matrix
"""

import numpy as np


def svd_2x2_singular_values(A):
    mat_ATA = A.T @ A
    theata = 0.5 * np.arctan2(2 * mat_ATA[0][1], mat_ATA[0][0] - mat_ATA[1][1])
    mat_J = np.array([[np.cos(theata), -np.sin(theata)], [np.sin(theata), np.cos(theata)]])
    mat_iter = mat_J.T @ mat_ATA @ mat_J
    SVD = (mat_J, np.sqrt(np.diag(mat_iter)), mat_J.T)
    return SVD


if __name__ == "__main__":
    A = np.array([[2, 1], [1, 2]])
    print(svd_2x2_singular_values(A))
