"""
Reshape Matrix (easy)

Write a Python function that reshapes a given matrix into a specified shape.

Example:
        input: a = [[1,2,3,4],[5,6,7,8]], new_shape = (4, 2)
        output: [[1, 2], [3, 4], [5, 6], [7, 8]]
        reasoning: The given matrix is reshaped from 2x4 to 4x2.
"""


def reshape_matrix(a, new_shape):
    reshaped_matrix = []
    a = sum(a, [])
    i = 0
    while i < new_shape[0] * new_shape[1]:
        reshaped_matrix.append(a[i : i + new_shape[1]])
        i += new_shape[1]
    return reshaped_matrix


if __name__ == "__main__":
    a = [[1, 2, 3, 4], [5, 6, 7, 8]]
    print(reshape_matrix(a, (4, 2)))
