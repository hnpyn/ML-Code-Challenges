"""
Matrix times Vector (easy)

Write a Python function that takes the dot product of a matrix and a vector.
return -1 if the matrix could not be dotted with the vector

Example:
        input: a = [[1,2],[2,4]], b = [1,2]
        output:[5, 10] 
        reasoning: 1*1 + 2*2 = 5;
                   1*2+ 2*4 = 10
"""


def matrix_dot_vector(a, b):
    if len(a) == 0 or len(b) == 0:
        return -1
    if len(a[0]) != len(b):
        return -1
    c = []
    for row in a:
        res = 0
        for i, j in zip(row, b):
            res += i * j
        c.append(res)
    return c


if __name__ == "__main__":
    a = [[1, 2], [2, 4]]
    b = [1, 2]
    print(matrix_dot_vector(a, b))
