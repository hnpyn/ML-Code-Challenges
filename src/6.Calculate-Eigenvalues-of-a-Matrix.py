"""
Calculate Eigenvalues of a Matrix (medium)

Write a Python function that calculates the eigenvalues of a 2x2 matrix. The function should return a list containing
the eigenvalues, sort values from highest to lowest.

Example:
        input: matrix = [[2, 1], [1, 2]]
        output: [3.0, 1.0]
        reasoning: The eigenvalues of the matrix are calculated using the characteristic equation of the matrix, which
        for a 2x2 matrix is λ^2 - tr(A)λ + det(A) = 0, where λ are the eigenvalues.
"""


def calculate_eigenvalues(matrix):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    trace = a + d
    det = a * d - b * c
    eigenvalues = [
        (-(-trace) + ((-trace) ** 2 - 4 * 1 * det) ** 0.5) / (2 * 1),
        (-(-trace) - ((-trace) ** 2 - 4 * 1 * det) ** 0.5) / (2 * 1),
    ]
    return eigenvalues


if __name__ == "__main__":
    matrix = [[2, 1], [1, 2]]
    print(calculate_eigenvalues(matrix))
