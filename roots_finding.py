import newtonRaphson
import secantMethod
import bisection_method

function = lambda x: x**3 - 2*x - 5
while True:
    inp = int(input("choose method:\n1. Newton-Raphson\n2. Secant\n3. Bisection\n"))
    if inp == 1:
        section_start = int(input("Enter the start of the section: "))
        section_end = int(input("Enter the end of the section: "))
        newtonRaphson.find_roots_in_section(function, section_start, section_end)
        break
    elif inp == 2:
        x1 = float(input("Enter the first initial guess: "))
        x2 = float(input("Enter the second initial guess: "))
        secantMethod.secant_method(function, x1, x2)
        break
    elif inp == 3:
        try:
            a = float(input("Enter the start value (a): "))
            b = float(input("Enter the end value (b): "))
            tol = float(input("Enter the tolerable error (default 1e-6): ") or 1e-6)
            if a > b:
                a, b = b, a
            if function(a) * function(b) >= 0:
                raise ValueError("The scalars a and b do not bound a root. Please choose a different interval.")
            root = bisection_method.bisection_method(function, a, b, tol)
            print(f"\nThe equation f(x) has an approximate root at x = {root:.6f}")

        except ValueError as e:
            print(f"Input Error: {e}")
        except RuntimeError as e:
            print(f"Runtime Error: {e}")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")


