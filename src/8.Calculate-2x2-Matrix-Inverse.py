"""
Calculate 2x2 Matrix Inverse (medium)

Write a Python function that calculates the inverse of a 2x2 matrix. Return 'None' if the matrix is not invertible.

Example:
        input: matrix = [[4, 7], [2, 6]]
        output: [[0.6, -0.7], [-0.2, 0.4]]
        reasoning: The inverse of a 2x2 matrix [a, b], [c, d] is given by (1/(ad-bc)) * [d, -b], [-c, a], 
        provided ad-bc is not zero.
"""


def inverse_2x2(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0:
        return None
    inverse = [
        [matrix[1][1] / det, -matrix[0][1] / det],
        [-matrix[1][0] / det, matrix[0][0] / det],
    ]
    return inverse


if __name__ == "__main__":
    matrix = [[4, 7], [2, 6]]
    print(inverse_2x2(matrix))
