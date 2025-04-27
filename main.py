import numpy as np
from math import pi
from numpy.linalg import norm

def is_diagonally_dominant(mat):
    if mat is None:
        return False

    d = np.diag(np.abs(mat))  # Find diagonal coefficients
    s = np.sum(np.abs(mat), axis=1) - d  # Find row sum without diagonal
    return np.all(d > s)

def partial_pivoting_with_vector(A, b):
    """
    Performs partial pivoting on matrix A and vector b.

    :param A: 2D numpy array (matrix)
    :param b: 1D numpy array (vector)
    :return: Tuple of (A, b) after pivoting
    """
    n = len(A)
    for i in range(n):
        # Find the pivot row with the largest absolute value in the current column
        pivot_row = i + np.argmax(np.abs(A[i:, i]))

        # Swap rows in A
        if pivot_row != i:
            A[[i, pivot_row]] = A[[pivot_row, i]]
            # Swap corresponding elements in b
            b[[i, pivot_row]] = b[[pivot_row, i]]

    return A, b

def fix(matrix, b):
    """
    Rearranges the rows and columns of a matrix to make it diagonally dominant.
    :param matrix: A square matrix (2D list or numpy array)
    :param b: A vector (1D list or numpy array)
    :return: A tuple containing the diagonally dominant matrix and the modified vector
    """
    n = len(matrix)
    matrix = np.array(matrix, dtype=np.float64)
    b = np.array(b, dtype=np.float64)

    for i in range(n):
        # Find the row with the largest absolute value in column i
        max_row = i
        for j in range(i, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j

        # Swap rows in the matrix and the vector if necessary
        if max_row != i:
            matrix[[i, max_row]] = matrix[[max_row, i]]
            b[i], b[max_row] = b[max_row], b[i]

        # Check if the diagonal element is dominant
        if abs(matrix[i][i]) < sum(abs(matrix[i][j]) for j in range(n) if j != i):
            raise ValueError("Cannot make the matrix diagonally dominant.")

    return matrix, b

def gauss_seidel(A, b, X0, TOL=0.00001, N=200):
    n = len(A)
    k = 1

    if is_diagonally_dominant(A):
        print('Matrix is diagonally dominant - preforming gauss seidel algorithm\n')

    print( "Iteration" + "\t\t\t".join([" {:>12}".format(var) for var in ["x{}".format(i) for i in range(1, len(A) + 1)]]))
    print("-----------------------------------------------------------------------------------------------")
    x = np.zeros(n, dtype=np.double)
    while k <= N:

        for i in range(n):
            sigma = 0
            for j in range(n):
                if A[i][i] == 0:
                    raise ZeroDivisionError(f"Zero on diagonal at row {i}, cannot divide by zero.")
                if j != i:
                    sigma += A[i][j] * x[j]
            x[i] = (b[i] - sigma) / A[i][i]

        print("{:<15} ".format(k) + "\t\t".join(["{:<15} ".format(val) for val in x]))

        if norm(x - X0, np.inf) < TOL:
            return tuple(x)

        k += 1
        X0 = x.copy()

    print("Maximum number of iterations exceeded")
    return tuple(pi, pi, pi)

def jacobi_iterative(A, b, X0, TOL=0.00001, N=200):
    n = len(A)
    k = 1

    if is_diagonally_dominant(A):
        print('Matrix is diagonally dominant - preforming jacobi algorithm\n')

    print( "Iteration" + "\t\t\t".join([" {:>12}".format(var) for var in ["x{}".format(i) for i in range(1, len(A) + 1)]]))
    print("-----------------------------------------------------------------------------------------------")

    while k <= N:
        x = np.zeros(n, dtype=np.double)
        for i in range(n):
            sigma = 0
            for j in range(n):
                if A[i][i] == 0:
                    raise ZeroDivisionError(f"Zero on diagonal at row {i}, cannot divide by zero.")
                if j != i:
                    sigma += A[i][j] * X0[j]
            x[i] = (b[i] - sigma) / A[i][i]

        print("{:<15} ".format(k) + "\t\t".join(["{:<15} ".format(val) for val in x]))

        if norm(x - X0, np.inf) < TOL:
            return tuple(x)

        k += 1
        X0 = x.copy()

    print("Maximum number of iterations exceeded")
    return tuple(pi, pi, pi)





if __name__ == '__main__':

    matrixA = np.array([[4, 2, 0], [2, 10, 4], [0, 4, 5]])
    vectorB = np.array([2, 6, 5])
    X0 = np.zeros_like(vectorB)
    if not is_diagonally_dominant(matrixA):
        try:
            matrixA, vectorB = fix(matrixA, vectorB)
        except ValueError as e:
            print('the matrix is not diagonally dominant, moving to try')

    solution = ()
    x = int(input('Enter 1 for Gauss Seidel or 2 for Jacobi: '))
    if x == 1:
        try:
            solution = gauss_seidel(matrixA, vectorB, X0)
        except ZeroDivisionError as i:
            print(f"Zero on diagonal at row {i}, cannot divide by zero.")

    elif x == 2:
        matrixA, vectorB = partial_pivoting_with_vector(matrixA, vectorB)
        try:
            solution = jacobi_iterative(matrixA, vectorB, X0)
            if solution == (pi, pi, pi):
                print("The system does not converge")
            elif not (is_diagonally_dominant(matrixA)):
                print("\n Although there is no dominant diagonal the alApproximate solution is:", solution)
        except ZeroDivisionError as i:
            print(f"Zero on diagonal at row {i}, cannot divide by zero.")

    print("\nthe approximate solution:", solution)