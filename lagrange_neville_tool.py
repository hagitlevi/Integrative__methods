import lagrange
import neville
x_data = [1, 2, 3, 4]
y_data = [1, -4, -5, 16]
x_interpolate = 2.5  # Point for which we want to find the interpolated value

try:
    # Neville interpolation
    neville_result = neville.neville(x_data, y_data, x_interpolate)
    print(f"Neville Interpolation: The interpolated value at x = {x_interpolate} is y = {neville_result}")

    # Lagrange interpolation
    lagrange_result = lagrange.lagrange_interpolation(x_data, y_data, x_interpolate)
    print(f"Lagrange Interpolation: The interpolated value at x = {x_interpolate} is y = {lagrange_result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")