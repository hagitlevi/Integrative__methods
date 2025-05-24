import newtonRaphson
import secantMethod

function = lambda x: x**3 - 2*x - 5


inp = int(input("choose method:\n1. Newton-Raphson\n2. Secant\n3. Bisection\n"))
if inp == 1:
    section_start = int(input("Enter the start of the section: "))
    section_end = int(input("Enter the end of the section: "))
    newtonRaphson.find_roots_in_section(function, section_start, section_end)

elif inp == 2:
    x1 = float(input("Enter the first initial guess: "))
    x2 = float(input("Enter the second initial guess: "))
    secantMethod.secant_method(function, x1, x2)

elif inp == 3:




else:
    print("Invalid choice. Please select 1, 2, or 3.")


