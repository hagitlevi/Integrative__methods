import math

def max_steps(a, b, err):
    """
    Calculate the maximum number of iterations required to reach the desired accuracy.
    """
    if err <= 0 or b <= a:
        raise ValueError("Invalid input: ensure b > a and err > 0.")
    s = math.ceil(math.log2((b - a) / err))
    return s


def bisection_method(f, a, b, tol=1e-6, verbose=True):
    """
    Perform the bisection method to find the root of a function.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("The scalars a and b do not bound a root. f(a) and f(b) must have opposite signs.")

    c, k = 0, 0
    steps = max_steps(a, b, tol)

    if verbose:
        print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "Iteration", "a", "b", "f(a)", "f(b)", "c", "f(c)"))

    while abs(b - a) > tol and k < steps:
        c = (a + b) / 2  # Midpoint
        f_c = f(c)

        if verbose:
            print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f}".format(
                k, a, b, f(a), f(b), c, f_c))

        if abs(f_c) < tol:  # Root found
            return c

        if f_c * f(a) < 0:
            b = c
        else:
            a = c

        k += 1

    if k == steps:
        raise RuntimeError("Maximum number of iterations reached without convergence.")

    return c


if __name__ == '__main__':
    # Define the function
    f = lambda x:  x**3 - x-1  # Example: Change this to your desired function

    # Input values
    try:
        a = float(input("Enter the start value (a): "))
        b = float(input("Enter the end value (b): "))
        tol = float(input("Enter the tolerable error (default 1e-6): ") or 1e-6)
        if a > b:
            a, b = b, a

        # Validate the interval
        if f(a) * f(b) >= 0:
            raise ValueError("The scalars a and b do not bound a root. Please choose a different interval.")

        # Call the bisection method
        root = bisection_method(f, a, b, tol)
        print(f"\nThe equation f(x) has an approximate root at x = {root:.6f}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except RuntimeError as e:
        print(f"Runtime Error: {e}")