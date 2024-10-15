"""
Determinant of a 4x4 Matrix using Laplace's Expansion (hard)
Write a Python function that calculates the determinant of a 4x4 matrix using Laplace's Expansion method. 
The function should take a single argument, a 4x4 matrix represented as a list of lists, and return the 
determinant of the matrix. The elements of the matrix can be integers or floating-point numbers. Implement 
the function recursively to handle the computation of determinants for the 3x3 minor matrices.

Example:
        input: a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        output: 0
        reasoning: Using Laplace's Expansion, the determinant of a 4x4 matrix is calculated by expanding it
        into minors and cofactors along any row or column. Given the symmetrical and linear nature of this 
        specific matrix, its determinant is 0. The calculation for a generic 4x4 matrix involves more complex 
        steps, breaking it down into the determinants of 3x3 matrices.
"""


def determinant_4x4(matrix):
    if len(matrix) == 0:
        return 0
    if len(matrix) == 1:
        return matrix[0][0]
    det = 0
    for col in range(len(matrix[0])):
        minor = [row[:col] + row[col + 1 :] for row in matrix[1:]]
        det += matrix[0][col] * ((-1) ** (0 + col)) * determinant_4x4(minor)
    return det


if __name__ == "__main__":
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(determinant_4x4(a))
