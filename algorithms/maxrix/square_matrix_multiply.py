def square_matrix_multiply(A, B):
    n = len(A)
    C = [[0 for _ in range(0, n)] for _ in range(0, n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


if __name__ == '__main__':
    A = [[1, 3], [7, 5]]
    B = [[6, 8], [4, 2]]
    C = square_matrix_multiply(A, B)
    for i in range(len(C)):
        print(C[i])
