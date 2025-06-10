from colors import bcolors
import main
from math import pi

def gauss_seidel(A, b, X0, TOL=0.00001, N=200):
    n = len(A)
    k = 1
    x = [0.0 for _ in range(n)]
    while k <= N:

        for i in range(n):
            sigma = 0
            for j in range(n):
                if A[i][i] == 0:
                    raise ZeroDivisionError(f"Zero on diagonal at row {i}, cannot divide by zero.")
                if j != i:
                    sigma += A[i][j] * x[j]
            x[i] = (b[i] - sigma) / A[i][i]

        max_diff = max(abs(x[i] - X0[i]) for i in range(n))
        if max_diff < TOL:
            return tuple(x)

        k += 1
        X0 = x.copy()

    raise  ValueError ("Maximum number of iterations exceeded. The solution did not converge.")




def polynomialInterpolation(table_points, x):
    matrix = [[point[0] ** i for i in range(len(table_points))] for point in table_points]  # Create the Vandermonde matrix
    b = [point[1] for point in table_points]  # Extract the vector b

    # Solve the system using Gauss-Seidel
    matrix1 = main.custom_array(matrix)
    b1 = main.custom_array(b)
    X0 = [0.0] * len(matrix1)
    if not main.is_diagonally_dominant(matrix1):
        try:
            matrix1, vector1 = main.fix(matrix1, b1)
        except ValueError as e:
            print(' ')
    try:
        matrixSol = gauss_seidel(matrix1, b1, X0=[0.0] * len(b))
    except ValueError as e:
        print(f"Error during Gauss-Seidel: {e}")
        return None

    result = sum([matrixSol[i] * (x ** i) for i in range(len(matrixSol))])  # Compute the polynomial value
    return result


