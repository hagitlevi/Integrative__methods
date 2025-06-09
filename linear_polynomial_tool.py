import linear_interpolation
import polynomial_interpolation

table_points = [(1, 0.8415), (2, 0.9093), (3, 0.1411)]
x_interpolate = 2.5  # Point for which we want to find the interpolated value

try:
    # Polynomial interpolation
    polynomial_result = polynomial_interpolation.polynomialInterpolation(table_points, x_interpolate)
    print(f"\nPolynomial Interpolation: The interpolated value at x = {x_interpolate} is y = {polynomial_result}")

    # linear interpolation
    linear_result = linear_interpolation.linearInterpolation(table_points, x_interpolate)
    print(f"Linear Interpolation: The interpolated value at x = {x_interpolate} is y = {linear_result}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")