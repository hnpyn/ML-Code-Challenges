"""
Transpose of a Matrix (easy)

Write a Python function that computes the transpose of a given matrix.

Example:
        input: a = [[1,2,3],[4,5,6]]
        output: [[1,4],[2,5],[3,6]]
        reasoning: The transpose of a matrix is obtained by flipping rows and columns.
"""


def transpose_matrix(a):
    if len(a) == 0 or len(a[0]) == 0:
        return -1
    b = []
    for i in zip(*a):
        b.append(list(i))
    return b


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    print(transpose_matrix(a))
