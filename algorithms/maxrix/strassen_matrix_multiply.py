import random
import numpy as np


def strassen(A, B):
    if type(A) is int:
        return A * B
    m = len(A)
    n = len(B)
    if m == 1 and n == 1:
        return A[0] * B[0]

    s_1 = minus_matrix(divide_matrix(B, 1, 2), divide_matrix(B, 2, 2))
    s_2 = plus_matrix(divide_matrix(A, 1, 1), divide_matrix(A, 1, 2))
    s_3 = plus_matrix(divide_matrix(A, 2, 1), divide_matrix(A, 2, 2))
    s_4 = minus_matrix(divide_matrix(B, 2, 1), divide_matrix(B, 1, 1))
    s_5 = plus_matrix(divide_matrix(A, 1, 1), divide_matrix(A, 2, 2))
    s_6 = plus_matrix(divide_matrix(B, 1, 1), divide_matrix(B, 2, 2))
    s_7 = minus_matrix(divide_matrix(A, 1, 2), divide_matrix(A, 2, 2))
    s_8 = plus_matrix(divide_matrix(B, 2, 1), divide_matrix(B, 2, 2))
    s_9 = minus_matrix(divide_matrix(A, 1, 1), divide_matrix(A, 2, 1))
    s_10 = plus_matrix(divide_matrix(B, 1, 1), divide_matrix(B, 1, 2))

    p_1 = strassen(divide_matrix(A, 1, 1), s_1)
    # print(f'p_2, {s_2}, {divide_matrix(B, 2, 2)}')
    p_2 = strassen(s_2, divide_matrix(B, 2, 2))
    p_3 = strassen(s_3, divide_matrix(B, 1, 1))
    p_4 = strassen(divide_matrix(A, 2, 2), s_4)
    p_5 = strassen(s_5, s_6)
    p_6 = strassen(s_7, s_8)
    p_7 = strassen(s_9, s_10)

    C11 = minus_matrix(plus_matrix(p_5, p_4), minus_matrix(p_2, p_6))
    C12 = plus_matrix(p_1, p_2)
    C21 = plus_matrix(p_3, p_4)
    C22 = minus_matrix(plus_matrix(p_5, p_1), plus_matrix(p_3, p_7))

    C = merge_matrix(C11, C12, C21, C22)

    return C


def divide_matrix(matrix, m, n):
    length = len(matrix)
    if length == 2:
        return matrix[m-1][n-1]
    sub_matrix = [[0 for _ in range(length // 2)] for _ in range(length // 2)]
    for i, matrix_i in enumerate(range((m - 1) * length // 2, m * length // 2)):
        for j, matrix_j in enumerate(range((m - 1) * length // 2, m * length // 2)):
            sub_matrix[i][j] = int(matrix[matrix_i][matrix_j])
    return sub_matrix


def merge_matrix(C11, C12, C21, C22):
    C = [[0 for _ in range(2)] for _ in range(2)]
    C[0][0] = C11
    C[0][1] = C12
    C[1][0] = C21
    C[1][1] = C22
    return C


def plus_matrix(A, B):
    if type(A) is int:
        return A + B
    m = len(A)
    n = len(B)
    if m == 1 and n == 1:
        return A[0] + B[0]
    C = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            C[i][j] = plus_matrix([A[i][j]], [B[i][j]])
    return C


def minus_matrix(A, B):
    if type(A) is int:
        return A - B
    m = len(A)
    n = len(B)
    if m == 1 and n == 1:
        return A[0] - B[0]
    C = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            C[i][j] = minus_matrix(A[i][j], B[i][j])
    return C


def generate_matrix(m, n, lower=0, upper=0):
    C = [[random.randint(lower, upper) for _ in range(n)] for _ in range(m)]
    return C


if __name__ == '__main__':
    A = generate_matrix(4, 4, -10, 20)
    B = generate_matrix(4, 4, -10, 20)
    # A = [[1, 3],
    #      [7, 5]]
    # B = [[6, 8],
    #      [4, 2]]

    print('\n'.join('\t'.join(map(str, row)) for row in A))
    print()
    print('\n'.join('\t'.join(map(str, row)) for row in B))
    print()
    C = strassen(A, B)
    print()
    print('\n'.join('\t'.join(map(str, row)) for row in C))
    C = np.dot(A, B)
    print()
    print('verif')
    print('\n'.join('\t'.join(map(str, row)) for row in C))

