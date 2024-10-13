"""
Matrix times Matrix (medium)

multiply two matrices together (return -1 if shapes of matrix dont aline), i.e. C = A dot product B
 
Example 1:
        input: A = [[1,2],
                    [2,4]], 
               B = [[2,1],
                    [3,4]]
        output:[[ 8,  9],
                [16, 18]]
        reasoning: 1*2 + 2*3 = 8;
                   2*2 + 3*4 = 16;
                   1*1 + 2*4 = 9;
                   2*1 + 4*4 = 18
                    
Example 2:
        input: A = [[1,2],
                    [2,4]], 
               B = [[2,1],
                    [3,4],
                    [4,5]]
        output: -1
        reasoning: the length of the rows of A does not equal
          the column length of B
"""


def matrixmul(a, b):
    if len(a[0]) != len(b):
        return -1
    c = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            row.append(sum([a[i][k] * b[k][j] for k in range(len(b))]))
        c.append(row)
    return c


if __name__ == "__main__":
    A = [[1, 2], [2, 4]]
    B = [[2, 1], [3, 4]]
    print(matrixmul(A, B))
