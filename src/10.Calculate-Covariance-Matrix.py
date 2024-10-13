"""
Calculate Covariance Matrix (medium)

Write a Python function that calculates the covariance matrix from a list of vectors. Assume that the input list
represents a dataset where each vector is a feature, and vectors are of equal length.

Example:
        input: vectors = [[1, 2, 3], [4, 5, 6]]
        output: [[1.0, 1.0], [1.0, 1.0]]
        reasoning: The dataset has two features with three observations each. The covariance between each pair of 
        features (including covariance with itself) is calculated and returned as a 2x2 matrix.
"""


def calculate_covariance_matrix(vectors):
    num_vecters = len(vectors)
    num_observations = len(vectors[0])
    means = [sum(v) / num_observations for v in vectors]
    covariance_matrix = [[0] * num_vecters for _ in range(num_vecters)]
    for i in range(num_vecters):
        for j in range(i, num_vecters):
            covariance_matrix[i][j] = sum(
                [
                    (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
                    for k in range(num_observations)
                ]
            ) / (num_observations - 1)
            covariance_matrix[j][i] = covariance_matrix[i][j]
    return covariance_matrix


if __name__ == "__main__":
    vectors = [[1, 2, 3], [4, 5, 6]]
    print(calculate_covariance_matrix(vectors))
