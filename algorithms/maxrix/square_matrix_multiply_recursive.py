def square_matrix_multiply_recursive(A, B):
    if type(A) is int:
        A = [A]
    if type(B) is int:
        B = [B]
    n = len(A)
    C = [[0 for _ in range(0, n)] for _ in range(0, n)]
    if n == 1:
        C = A[0] * B[0]
        return C

    C[0][0] = square_matrix_multiply_recursive(A[0][0], B[0][0]) + square_matrix_multiply_recursive(A[0][1], B[1][0])
    C[0][1] = square_matrix_multiply_recursive(A[0][0], B[0][1]) + square_matrix_multiply_recursive(A[0][1], B[1][1])
    C[1][0] = square_matrix_multiply_recursive(A[1][0], B[0][0]) + square_matrix_multiply_recursive(A[1][1], B[1][0])
    C[1][1] = square_matrix_multiply_recursive(A[1][0], B[0][1]) + square_matrix_multiply_recursive(A[1][1], B[1][1])
    return C

if __name__ == '__main__':
    A = [[1, 3],
         [7, 5]]
    B = [[6, 8],
         [4, 2]]
    C = square_matrix_multiply_recursive(A, B)
    for i in range(len(C)):
        print(C[i])