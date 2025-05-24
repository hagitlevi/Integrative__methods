import newtonRaphson

function = lambda x: x**3 - 2*x - 5
section_start = 1
section_end = 3


inp = int(input("choose method:\n1. Newton-Raphson\n2. Bisection\n3. Secant\n"))
if inp == 1:
    newtonRaphson.find_roots_in_section(function, section_start, section_end)
elif inp == 2:

