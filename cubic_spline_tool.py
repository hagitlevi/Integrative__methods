import cubic_spline
from math import pi
from colors import bcolors

x_data = [0, pi/6, pi/4, pi/3, pi/2]
y_data = [0, 0.5, 0.7071, 0.8660, 1.0]
x_interpolate = pi/3  # Point for which we want to find the interpolated value

try:
    # Cubic Spline interpolation
    cubic_spline_result = cubic_spline.cubicSplineInterpolation(x_data, y_data, x_interpolate)
    print(bcolors.OKBLUE + f"Cubic Spline Interpolation: The interpolated value at x = {x_interpolate} is y = {cubic_spline_result}" + bcolors.ENDC)

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")