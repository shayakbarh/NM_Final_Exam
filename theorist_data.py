import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import newton
import matplotlib.pyplot as plt
import requests

# Load the data from the provided URL
data_url = "https://theory.tifr.res.in/~kulkarni/data.txt"
response = requests.get(data_url)
data = np.genfromtxt(data_url, dtype=None, encoding=None)

# Extract theta and d values from the data
theta_values = data[:, 0].astype(float)
d_values = data[:, 1].astype(float)

# (a) 

# Cubic spline interpolation function
cubic_interp = CubicSpline(theta_values, d_values)

def interpolate_d(theta):
    
    # Ensure theta is within the range [0.1, 10]
    theta = np.clip(theta, 0.1, 10.0)

    # Use cubic spline interpolation to find the corresponding d value
    interpolated_d = cubic_interp(theta)

    return interpolated_d

# (b) 
# Plot the theorist's data
plt.scatter(theta_values, d_values, label="Theorist's Data")

# Plot the cubic spline interpolation curve
theta_range = np.linspace(0.1, 10, 100)
d_interpolated = interpolate_d(theta_range)
plt.plot(theta_range, d_interpolated, label="Cubic Spline Interpolation", color = 'red')

plt.xlabel("Theta")
plt.ylabel("d")
plt.title(" Q5: Theorist's Data and Cubic Spline Interpolation")
plt.legend()
plt.grid()
plt.show()

# (c)
# Root finding using Newton-Raphson method
target_d = 3704

inferred_theta = newton(cubic_interp, x0=5.0)  # You can adjust the initial guess (x0) as needed

print(f"Theoretical theta corresponding to d = {target_d} units: {inferred_theta}")




